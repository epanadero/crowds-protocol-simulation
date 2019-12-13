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
  Can be "initiator" or "last-honest". If broken-paths is 0, the this is never applied. Still, it must be provided.
  This determines the recovery method applied when an adversary breaks a path.<br/>
  If set to "initiator", then the sender must rebuild the path from the beginning.<br/>
  If set to "last-honest", then the previous user before the corrupt user that just detected them must try to forward again.
