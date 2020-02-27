# Crowds anonymity protocol simulation

You can run the simulation with python3 as follows:
```sh
$ python3 simulate.py <phi> <graph-file> <corrupted-file> <users-file> <broken-paths> <fix-strategy>
```
The simulation receives as input the following arguments:
- phi<br/>
  Forwarding probability

- graph-file<br/>
  The adjacency matrix of the users. This is expected to be an n x n matrix<br/>
  e.g.<br/>
  ```sh
  0 1 0
  1 0 1
  0 1 0
  ```
  From this file the number of users is determined. Their ids are in ascending order.<br/>
  The matrix above corresponds to the following users:<br/>
  user[id=0] connected with (user[id=1])<br/>
  user[id=1] connected with (user[id=0], user[id=2])<br/>
  user[id=2] connected with (user[id=1])<br/>

- corrupted-file<br/>
  The ids of the corrupt users, one id per line (0, num_users-1]

- users-file<br/>
  One id per line for the users that will attempt to send a message, duplicates are
  allowed of course, ids of users found in corrupted-file are not allowed in this file

- broken-paths<br/>
The number of paths the corrupted users can break for each sending

- fix-strategy<br/>
  Can be "initiator" or "last-honest". If broken-paths is 0, the this is never applied. Still, it must be provided. This determines the recovery method applied when an adversary breaks a path.<br/>
  If set to "initiator", then the sender must rebuild the path from the beginning.<br/>
  If set to "last-honest", then the previous user before the corrupt user that just detected them must try to forward again.<br/>
# Output
The output of the simulations is as follows: For each sending, produce a line that starts with sender_id: and continue with a space-separated list of the users that were detected during this sending. The output is printed to the console so that you may redirect it wherever you wish.<br/>
e.g. <br/>
```sh
0: 1 2
0: 0 0
1: 1 3 2
  ```
This means that user 0 sent two messages. The first time, users 1 and 2 were detected by a corrupt user and the second time the user themselves got detected twice. User 1 sent one message and users 1,3 and 2 got detected during that sending.

# Generate users file automatically
You may also generate a users-file automatically by running
```sh
$ python3 generate_users_file.py <apriori-file> <num-iterations>
```
- apriori-file<br/>
The apriori knowledge the adversary has about the users. For each line, which also corresponds to a user id, provide the probability at which the user with id 'number of line-1' sends messages in the network. Corrupt users should have 0, but this is not checked in this context. The sum of the float numbers in this file must be 1.
- num-iterations<br/>
This is the total number of sendings that will be generated. Therefore, for each user i, apriori\[i\]\*num_iterations sendings are generated by this script file.<br/>
The output is directed to stdout so that you may redirect it wherever you wish. 
