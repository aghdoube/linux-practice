# Systems Administration & Engineering Practice Log

This is my personal log of the work I've been doing while learning the foundations of cloud engineering. I've been keeping track of the commands I've used, mistakes I've made, problems I've run into, and things I've had to look up along the way. Some topics took longer than others, especially when I was unfamiliar with the syntax or couldn't get a command to work as expected.

---

### Module 1: Linux Command Line Foundations & Automation

I started with the Linux command line and spent time getting comfortable with navigating directories, managing files, working with processes, and using basic commands. At first, I had to look up quite a few things, but repeating the commands helped me get more familiar with the terminal.

**Things I practised and problems I ran into:**

*   **Bash spacing:** One thing that caught me out was the spacing in Bash conditions. When using `if [ ]`, I found that leaving out a space in the wrong place caused errors. It took a few attempts before I got used to the syntax.
*   **Variable names:** I also found out that Bash variables cannot contain hyphens. Some of my variable names weren't working, and changing them to use underscores fixed the issue.
*   **Apt remove vs purge:** I practised removing packages and noticed the difference between `apt remove` and `apt purge`. Remove uninstalls the package but can leave configuration files behind, while purge removes those configuration files as well.
*   **Managing processes:** I worked with background and foreground processes using `Ctrl + Z`, `bg`, and `fg`. I also used `ps aux` to check running processes and practised stopping processes with `kill`.
*   **Other commands:** I spent time using `find` to locate files and folders, and practised sorting and filtering text with `uniq -c` and `uniq -u`. I also worked through some OverTheWire challenges to get more comfortable solving problems without relying on instructions for every step.

---

### Module 2: Networking & Understanding Cloud Environments

After Linux, I moved on to networking. I started learning how IP addresses, subnets, ports, and firewalls fit together and how they affect communication between different systems.

**Things I practised and problems I ran into:**

*   **Missing utilities:** When I first tried using `nslookup`, the command wasn't available in my environment. I had to update the package lists and install `dnsutils` before I could use it.
*   **Checking network interfaces:** I used `ip addr show` to inspect the network interfaces on my machine. This helped me understand how the system was connected. My active interface was `eth0`, with the IP address `10.0.10.169/16`.
*   **Traceroute:** One issue I spent time looking into was running `traceroute google.com`. After the first few hops, the output kept showing `* * *`. Initially, I thought I had done something wrong, but I learned that some cloud environments filter or block the packets used by traceroute. This meant I couldn't see every hop, even though the command itself was working.

---

### Module 3: Python Basics & File Operations

Once I was more comfortable with the command line, I started working with Python. Since I already had some experience with JavaScript, I tried comparing the two languages to understand what was different.

**Things I practised and problems I ran into:**

*   **Indentation:** One of the first differences I noticed was how Python uses indentation instead of curly brackets to structure code. I had to pay more attention to spacing, especially when switching between Python and JavaScript.
*   **Naming differences:** I also got used to some of the differences in terminology and syntax. Python uses `True` and `False` for booleans, lists for collections of items, and dictionaries for storing key-value pairs.
*   **Writing and testing code:** File operations were something I initially struggled with, so I decided not to rush through them. I started writing smaller sections of code, testing each one in Git Bash, and fixing any errors before moving on.
*   **Monitoring script:** I eventually put together a small server monitoring script that worked with a list of dictionaries to check CPU information. I also added a `try/except` block so that incorrect or missing telemetry data wouldn't immediately stop the script.

---

### Module 4: Relational Databases & SQL

I then moved on to SQL and started learning how relational databases work. I wanted to understand how tables connect to each other and how information can be stored and retrieved.

**Things I practised and problems I ran into:**

*   **Setting up SQLite:** I opened a SQLite database through the terminal and created two tables: `customers` and `orders`. I used `.tables` to check that both tables had been created.
*   **UPDATE mistakes:** While entering test data, I accidentally assigned orders to the wrong customers and entered Hamburg instead of Berlin for one of the customer locations. I had to correct the records using `UPDATE`. This also taught me to be careful with the `WHERE` clause. Without it, an update can affect every row in the table.
*   **Queries and JOINs:** I practised using `SELECT` to retrieve records, deleting test entries, and joining the two tables together. The first time I got the customer names and their corresponding orders showing correctly in one result was a good moment because I could actually see how the tables related to each other.

---

### Module 5: Practical Troubleshooting & Mini-Server Lab

At this point, I realised that knowing individual commands wasn't enough. I needed to get better at using them together and figuring out what to check when something wasn't working.

I spent a week working on a small server project where I could put some of the Linux, networking, and scripting skills into practice.

**Things I practised and problems I ran into:**

*   **Nginx setup:** I installed Nginx and worked through the basic configuration. I then used `curl` and `wget` to send requests and check the responses from the web server, including status codes such as `200 OK` and `301 Redirect`.
*   **Checking services and logs:** I practised checking service status with `systemctl` and looking through files in `/var/log`. I also worked through simulated downtime scenarios where I had to find out why a service wasn't responding and restart it.
*   **Disk space:** I simulated a situation where a server was running low on storage. I used `df -h` to check available disk space and `du -sh` to investigate which directories were taking up the most room. This helped me understand how to narrow down the problem before deleting anything.
*   **Backups and cron jobs:** I practised creating compressed backups of configuration files using `tar -czf`. I then set up a cron job to run the backup script automatically at scheduled intervals.

---

### Overall Progress

Looking back at these modules, I've noticed that I learn much better by actually running commands and fixing problems than by just reading about them. Quite a few things that seemed confusing at first became easier after making mistakes and working out why something wasn't behaving as expected.

I'm still building confidence with Linux, networking, Python, and SQL, but I now have a better understanding of how these areas connect when working with a server. My next focus is to keep practising these skills through small projects rather than just moving from one topic to the next.
