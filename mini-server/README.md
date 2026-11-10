# Mini-Server: Linux Infrastructure Lab

A hands-on engineering lab focused on provisioning a local web server environment, managing system users, and automating critical directory backup pipelines.

## 🛠️ Implementation & Admin Tasks
*   **Web Server Engine:** Installed and configured Nginx to handle incoming local HTTP traffic, verifying status loops via `systemctl`.
*   **Access Control & Security:** Created dedicated system users (`anna`) and groups, mastering file ownership transfers (`chown`) and exclusive permissions matrices (`chmod`).
*   **Process & Node Management:** Monitored background daemons and kernel jobs using `ps aux`, `jobs`, and process control flags (`kill`).
*   **Disaster Recovery Automation:** Engineered a shell script execution path using `tar -czf` to compress project assets, fully automated via system `cron` schedules.
*   **Network Diagnostics:** Tested endpoint responses, port layouts, and status returns using low-level network utilities (`curl`, `wget`).

## 🔍 Key Troubleshooting Takeaways
*   **Permission Blocks:** Resolved an 'Operation not permitted' collision after altering file ownership, fixed by applying elevated privileges (`sudo chmod`).
*   **Error Logging:** Read through standard server trace printouts to locate configuration syntax bugs, converting individual commands into sequential pipeline automation.
