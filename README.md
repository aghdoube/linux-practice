# Linux, Systems & Automation Lab Workspace

This repository maps my daily engineering labs, operational Bash scripts, and configuration pipelines designed to build core systems competencies required for managing cloud architecture environments.

## 📁 Repository Architectural Matrix

*   **`automation-scripts/`**: Executable shell pipelines handling environment tasks.
    *   `server_deployer.sh`: Automated configuration script executing systemic `apt` updates and provisioning Nginx.
    *   `backup.sh`: Condition-bounded data backup logic verifying path criteria before generating system targets.
    *   `first_script.sh`: System telemetry checking hardware resources, node health metrics, and storage capacities.
    *   `workspace_setup.sh`: Scripted setup routine deploying standardized directory architectures.
    *   `myservice.sh`: Persistent runtime script emulating server background daemon behaviors.
*   **`operational-logs/`**: Raw diagnostic execution output traces tracking deployment history parameters.
*   **`database-tier/`**: Structured SQL playground configurations (`shop.db`, `sql.md`) tracing indices, updates, and key allocations.
*   **`python-runtime/`**: Backend infrastructure scripts practicing syntax execution, structural lookups, and JSON data mapping.
*   **`project-template/`**: Baseline configuration framework testing static parameters (`settings.conf`).
*   **`mini-server/`**: Dedicated Nginx engine workspace practicing localized user groups (`anna`), crontab schedules, and server automation utilities inside the `scripts/` directory.
*   **`playground/`**: Raw command trace archives detailing historical terminal labs.

---

## 📓 Engineering Log & Troubleshooting Logs

I maintain an active, evergreen field journal capturing the actual logic traps, networking errors, and storage constraints I fixed throughout these labs.

🔗 **[Review my troubleshooting notes inside JOURNAL.md](./JOURNAL.md)**

---

## 🚀 Execution Standards

To fire off any provisioning component within the script matrix, lock down the security permission bits to your isolated account user context:

```bash
# Enter the script location
cd automation-scripts/

# Enforce secure owner execution permissions
chmod 700 server_deployer.sh

# Initialize the automated execution tree
./server_deployer.sh
```
