#!/bin/bash
# PreToolUse hook for Edit/Write: blocks if file wasn't recently read or was modified since last read
set -euo pipefail

input=$(cat)
file_path=$(echo "$input" | jq -r '.tool_input.file_path // empty')

# Only enforce for files within the presentations repo
repo_dir="/home/ebi/presentations"
if [[ -z "$file_path" ]] || [[ "$file_path" != "$repo_dir"* ]]; then
  # Outside repo — allow without check
  jq -n '{
    "hookSpecificOutput": {
      "hookEventName": "PreToolUse",
      "permissionDecision": "allow"
    }
  }'
  exit 0
fi

tracker_dir="/tmp/presentations-read-tracker"
key=$(echo -n "$file_path" | md5sum | cut -d' ' -f1)
tracker_file="${tracker_dir}/${key}"

# Check 1: Was this file ever read in this session?
if [[ ! -f "$tracker_file" ]]; then
  jq -n --arg fp "$file_path" '{
    "hookSpecificOutput": {
      "hookEventName": "PreToolUse",
      "permissionDecision": "deny",
      "permissionDecisionReason": ("BLOCKED: " + $fp + " を編集する前に必ず Read で最新内容を読み直してください。人間が手動編集している可能性があります。")
    }
  }'
  exit 0
fi

# Check 2: Has the file been modified since we last read it?
if [[ -f "$file_path" ]]; then
  current_mtime=$(stat -c %Y "$file_path" 2>/dev/null || echo "0")
  recorded_mtime=$(cut -d'|' -f2 "$tracker_file")

  if [[ "$current_mtime" != "$recorded_mtime" ]]; then
    # Invalidate the stale record
    rm -f "$tracker_file"
    jq -n --arg fp "$file_path" '{
      "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": ("BLOCKED: " + $fp + " は前回の Read 以降に変更されています。最新内容を Read で読み直してから編集してください。")
      }
    }'
    exit 0
  fi
fi

# All checks passed — allow
jq -n '{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow"
  }
}'
exit 0
