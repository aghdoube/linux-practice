# My Learning Journal

# Day 1 [02.10.26]


Today I spent a total of 5 hours studying and practicing Linux. I am following Nana's TechWorld roadmap step-by-step. 

It was definitely not easy. I ran into a lot of problems, went through a ton of trial and error, and had to Google everything to figure out why things were breaking. But I kept trying until my scripts finally worked and pushed to GitHub.

Here are the official skills from the roadmap that I tackled today:

Key Linux Skills for Cloud Engineers
Command Line Proficiency: Become comfortable navigating and managing systems using the
terminal. Learn essential commands for file management, process control, and system monitoring.

File System Structure: Understand the Linux file system hierarchy, important directories, and how to
navigate between them.

File Permissions: Master the concepts of ownership, permissions (read, write, execute), and how to
modify them using chmod and chown commands.

Process Management: Learn how to start, stop, and monitor processes. Understand concepts like
foreground vs. background processes, job control, and process priorities.

Shell Scripting: Develop the ability to automate repetitive tasks by writing bash scripts. This includes
variables, conditionals, loops, and functions.

Package Management: Become familiar with package managers like apt, yum, or dnf for installing,
updating, and removing software.

System Logging: Know where logs are stored and how to analyze them for troubleshooting.

Ready for the next step tomorrow.



# Day 2  [03.10.26]

Did a quiz today to test everything I learned yesterday without looking at multiple choice options. It definitely showed me where I was rusty. I had to look things up on Stack Overflow and AskUbuntu to get the exact syntax right. I forgot that bash variables can't have hyphens, messed up the spacing inside an if statement bracket, and forgot that apt purge is what actually clears out config files instead of just apt remove. Also reviewed using find, checking logs in /var/log, and using ctrl+z and bg for background jobs. It took a lot of trial and error with typos but I fixed every command myself. 

On to networking....

Today I moved on from Linux and started Phase 1 Networking from Nana's roadmap. This was more conceptual than yesterday, so I spent most of the time going through the basic terms and then testing some of them in the terminal.

It took some extra digging to figure out why certain network commands weren't working out of the box or why some of the output looked strange in a cloud environment. But after looking things up, I got everything installed and started to understand what was actually happening.

Here are the official skills from the roadmap that I tackled today:

Key Networking Skills for Cloud Engineers

IP Addressing & CIDR: Understand how IP addresses work and how the `/16` part tells you how big the network is.

IPv4 vs IPv6: Understand the difference between IPv4 and IPv6, and why IPv6 was introduced because there aren't enough IPv4 addresses.

DNS (Domain Name System): Understand how DNS turns names like google.com into IP addresses.

Ports & Firewalls: Learn what ports are used for, like port 80 for HTTP and port 443 for HTTPS, and how firewalls allow or block traffic.

Routing & Load Balancing: Understand how packets move between different networks and how load balancers spread traffic across multiple servers.

VPN (Virtual Private Network): Understand how a VPN creates an encrypted connection over the internet.

For practice, I had to install `dnsutils` first because nslookup wasn't available, then used it to query google.com. I also used `ip addr show` to check my network interfaces and found eth0 with the address 10.0.10.169/16.

I tried `traceroute google.com` too to see how the traffic gets there, but after the local gateway it was basically just * * *. I thought something was wrong at first, but after looking into it I found that cloud environments can block or ignore the packets traceroute relies on. So it wasn't a broken command or a typo on my end.


