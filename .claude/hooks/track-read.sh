#!/bin/bash
# PostToolUse hook for Read: records file path + mtime for freshness tracking
set -euo pipefail

input=$(cat)
file_path=$(echo "$input" | jq -r '.tool_input.file_path // empty')

# Only track files within the presentations repo
repo_dir="/home/ebi/presentations"
if [[ -z "$file_path" ]] || [[ "$file_path" != "$repo_dir"* ]]; then
  exit 0
fi

# Record mtime of the file at time of read
tracker_dir="/tmp/presentations-read-tracker"
mkdir -p "$tracker_dir"

if [[ -f "$file_path" ]]; then
  mtime=$(stat -c %Y "$file_path" 2>/dev/null || echo "0")
  # Use base64-encoded path as filename to avoid slash issues
  key=$(echo -n "$file_path" | md5sum | cut -d' ' -f1)
  echo "${file_path}|${mtime}" > "${tracker_dir}/${key}"
fi

exit 0
