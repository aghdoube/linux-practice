# Day 7 - 8 - 9 [09.10 - 11.10.26]

This weekend (Friday 09.10 to today 11.10) I worked through the four foundations of Phase 1 in Nana’s roadmap: Linux CLI, networking, Python and databases. They’re starting to connect.

I started with Linux and learned more commands. I used sudo to run things with admin rights and find to search for files. I also learned uniq, with -c to count duplicate lines and -u to show only the lines that appear once. To practice, I played the OverTheWire game, and I learned a lot from it.

Next was networking. I learned the difference between public and private subnets and how IP addresses fit into that. I also learned how SSH works and what the main ports are for: port 22 for SSH, port 80 for HTTP and port 443 for HTTPS.

On Saturday afternoon I focused on databases. I read the theory first: tables, keys, SQL vs. NoSQL, managed vs. self-managed. It made sense on paper, but I wanted to try it myself.

In my Codespace I opened SQLite and built two tables, customers and orders. I checked them with .tables.

I also made mistakes with the data. Anna ended up in Hamburg instead of Berlin, and two orders were linked to the wrong customers. That gave me a good reason to practice UPDATE, and I learned to never forget the WHERE clause, or every row gets overwritten. I also tried SELECT filters, deleted the Mouse order, and ran my first JOIN. Seeing customer names next to their products from two tables was when it clicked.

I plan to officiale start on monday with Phase 2 of nanas roadmap # Cloud Service Models Explained #

ps: I’m still struggling with File I/O, so I’m putting it on the back burner for now and will come back to it later.
