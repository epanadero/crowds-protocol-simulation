This is a simulation of the crowds anonymity protocol.

You can run the simulation with python3 as follows:
python3 simulate.py <phi> <graph-file> <corrupted-file> <users-file> <broken-paths> <fix-strategy>

The simulation receives as input the following arguments:
1. phi: Forwarding probability

2. graph-file: The adjacency matrix of the users. This is expected to be an n x n matrix
e.g.
0 1 0
1 0 1
0 1 0

From this file the number of users is determined. Their ids are in ascending order.
The matrix above corresponds to the following users:
user[id=0] connected with (user[id=1])
user[id=1] connected with (user[id=0], user[id=2])
user[id=2] connected with (user[id=1])

3. corrupted-file: The ids of the corrupt users, one id per line (0, num_users-1]

4. users-file: One id per line for the users that will attempt to send a message, duplicates are
allowed of course, ids of users found in corrupted-file are not allowed in this file

5. broken-paths: The number of paths the corrupted users can break for each sending

6. fix-strategy: Can be "initiator" or "last-honest". If broken-paths is 0, the this is never applied. Still, it must be provided.
This determines the recovery method applied when an adversary breaks a path.
If set to "initiator", then the sender must rebuild the path from the beginning.
If set to "last-honest", then the previous user before the corrupt user that just detected them must try to forward again.
