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



# Day 3 [04.10.26]


Today I went back over everything from the first two days to make my Linux foundation solid before moving on. I started with a Linux review and then did a networking review. I could answer most of the permission, process and file questions at the first try, like chmod with numbers, ps aux, fg and bg, wc -l and combining grep with a pipe. For networking I could explain CIDR in my own words, including why a /16 is a bigger network than a /24, and I knew what the 301 and 200 status codes from curl mean.

Things i struggled with: kill with a job number, mkdir -p, the * wildcard, ls -a for hidden files, Ctrl+C vs. Ctrl+Z, router vs. port, and listening vs. established in ss. Those are the ones I need to learn.

After that I wrote a  Linux command cheat sheet to fill the gaps in my foundation. It covers navigation, files, searching, pipes and redirects, permissions, users and sudo, processes, apt and system info. I also added the topics a job-ready foundation needs on top of that: the folder layout (/etc, /var/log, /home, /tmp), systemctl, SSH, cron and simple bash scripts.

Next I'm going to type every command from the cheat sheet in the Codespace and build some muscle memory for the future.






# Day 4 [05.10.26]

Before moving on, I took a blind diagnostic on the core concepts from the roadmap and got 12 out of 12. So proud!!!

## Linux & CLI basics

- **Navigation:** `cd` to move around directories
- **System files:** config files live in `/etc`
- **Permissions:** `chmod` changes read, write and execute permissions
- **Processes:** `kill` stops a frozen program. If it's really stuck, `kill -9` forces it to shut down
- **Scripting:** `if` statements let a script make decisions
- **Packages:** `sudo apt` to install, update or remove software

## Cloud networking

- **Subnet sizing:** a `/24` gives 256 IPs, plenty for 100-200 servers
- **DNS:** basically a phone book that turns domain names into numbers
- **Routing:** a router looks at the destination IP and sends the packet the right way
- **Ports and firewalls:** ports are like doors for traffic. Port 80 is the default for plain HTTP
- **Load balancing:** spreads traffic across servers and skips the unhealthy ones
- **VPN:** an encrypted tunnel so private data can cross the normal internet safely

## Python

Started the programming basics section today. I already know the JavaScript fundamentals, so I wanted to see how much carries over to Python. Did another diagnostic on coding logic, syntax and error handling.

Python is way less fussy than JavaScript. No variable keywords, no semicolons, no curly braces. You just type the name and assign a value. Blocks start with a colon and a strict 4-space indent, and if the spacing is off, the script crashes.

I hit a few syntax errors while practicing. Nothing big, but it took a while to get used to how strict Python is about spacing.

Naming differences to remember: booleans are capitalized (`True`/`False`), arrays are called Lists, and objects are called Dictionaries.

By the end of the day I'd finished the basics for variables, conditionals, functions and `try/except`. File I/O is next, to see how Python reads and writes files.

Excited for tomorrow!!


# Day 5 and 6 [06.10 - 07.10.26]



Yesterday, on day 5, I started reading about File I/O. I wrote the syntax and the explanations in my notebook. I want to study this part slowly because it is an important part of cloud engineering. I understood some of the concepts, and others were a bit harder to grasp. I'm sure that with a little more time I will get there.

So I wouldn't forget what I learned before, today, on day 6, I went over everything again: the Linux basics, networking and the Python fundamentals. It felt good to see how much I already know. I went through it step by step to see what I really know and where I slip up. My logic is fine. It's my fingers that still fight the syntax. I kept forgetting the colon at the end of my if and else lines, I misspelled else a few times, i wrote else if, and I missed some closing brackets. Beginner mistakes, but fixing them one by one helped the rules finally stick.

What helped most was writing code in tiny steps. One line, test it in the terminal, and only add the next line when the first one works. With that I built a server monitoring function. It loops through a list of dictionaries, checks the CPU numbers, and uses try and except to handle bad data without crashing the script. Seeing it print the healthy, critical and invalid servers correctly in Git Bash felt really good.

Overall today made me feel more sure about the next steps. 
Tomorrow I'll go back to File I/O with fresh eyes and keep taking it one step at a time.
