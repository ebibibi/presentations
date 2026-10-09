It's time to update your devices to ensure connectivity to Windows Update moving forward.

Windows Update uses certificate-based trust to confirm that your devices are connecting to authoritative Windows Update servers, so that you can have confidence in the update content delivered to your devices. As a standard security practice, these certificates have an expiration date. This means that they eventually need to be rotated (that is, replaced by new certificates). A set of these certificates will expire on **May 17, 2027** and **June 19, 2027**.

While Microsoft is delivering solutions for most devices through normal monthly updates, some Windows versions will need IT action. If unaddressed, affected devices will stop connecting and receiving all types of updates from Windows Update. However, the key to getting updates from Windows Update beyond 2027 is to keep your devices up to date today.

> **Note:** This doesn't apply to devices receiving updates from Windows Server Update Services (WSUS).

## Identify and prepare devices that require action

Our goal is to accomplish this certificate rotation with minimal impact to your organization. In most cases, no action is required. That's your case if your devices are running an in-support version of Windows and are up to date with recent monthly quality updates. For older or out-of-date Windows versions, however, take action as recommended in the table and described below.

| Windows version | Action required |
| --- | --- |
| Windows 11, version 25H2 and later | None. |
| Windows 11, version 24H2 and Windows Server 2025 | Install the September 2025 Windows security update or later before **June 19, 2027**. |
| Other Windows 11 versions in support and Windows Server 2022 | Install the July 2026 Windows security update or later before **June 19, 2027**. |
| Windows 10 versions in support | Install the July 2026 Windows security update or later before **June 19, 2027**. |
| Long-Term Servicing Branch (LTSB)/Long-Term Servicing Channel (LTSC) releases of Windows 10 Enterprise 2019 LTSC, Windows Server 2019, and Windows Server 2016 | Install the July 2026 Windows security update or later before **May 17, 2027**. |
| Other Windows versions | Upgrade these devices to a supported version of Windows for [client](https://learn.microsoft.com/windows/release-health/supported-versions-windows-client) or [server](https://learn.microsoft.com/windows/release-health/windows-server-release-info). Because these devices are out of support, they'll lose access to Windows Update services. |

To find and access release notes for your versions of Windows, browse [Windows release health](https://learn.microsoft.com/windows/release-health/).

## What happens after the expiration date

**Devices on supported and updated versions of Windows**  
These devices continue receiving updates without interruption. They already have the necessary updated certificates.

**Devices on supported versions of Windows that aren't up to date**  
After the May and June 2027 certificate expiration dates, these devices won't be able access Windows Update services. Reference the table above to install the appropriate Windows security update or later depending on your OS version. These updates contain the new certificates. Use [Microsoft Update Catalog](https://learn.microsoft.com/troubleshoot/windows-client/installing-updates-features-roles/download-updates-drivers-hotfixes-windows-update-catalog) to directly download and install required updates on these devices. Alternatively, distribute them via your regular management tools.

**Devices on unsupported versions of Windows**  
These devices will lose access to Windows Update services and won't receive any updates as a result. We recommend upgrading to a supported version of Windows [client](https://learn.microsoft.com/windows/release-health/supported-versions-windows-client) or [server](https://learn.microsoft.com/windows/release-health/windows-server-release-info).

## Recommended action plan for IT admins

If your organization has devices that require action, here's your action plan:

1. Identify devices running older or unsupported versions of Windows.
2. Keep supported devices current with monthly Windows updates.
3. Create an upgrade plan for unsupported devices before May and June 2027.

## Start today for early readiness

Keep supported Windows devices current for a smooth certificate rotation. Doing this today has the following benefits beyond June 2027:

- Avoid update disruptions.
- Reduce security and compliance risk.
- Minimize last-minute remediation.
- Use the timeline to align upgrade, servicing, and lifecycle planning.

And if you do need to act on older device populations, there's still time! Review, update, and plan upgrades for unsupported versions before the May 2027 or June 2027 certificate expiration dates.

Have questions? Leave us a comment below or share your thoughts on our [discussion board post](https://aka.ms/WindowsUpdate2027CertificateRotation).

---

**Securing today. Preparing for what's next.**  
Learn more in the [Windows Security book](https://learn.microsoft.com/windows/security/book/) and  [Windows Server Security book](https://aka.ms/ws2025securitybook). To stay up to date on the latest in security features and enhancements, visit the [Microsoft Security site](https://www.microsoft.com/security/business), follow the [Microsoft Security Blog](https://www.microsoft.com/security/blog/), or connect with [Microsoft Security](https://www.linkedin.com/showcase/microsoft-security/) on LinkedIn and [@MSFTSecurity](https://twitter.com/@MSFTSecurity).

Version 2.0