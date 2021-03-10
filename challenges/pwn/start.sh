#!/usr/bin/env bash

cd cliff
./ynetd -p 12345 ./cliff &
cd ..

cd echo_back
./ynetd -p 12346 ./echo_back &
cd ..

cd simple_login
./ynetd -p 12347 ./simple_login &
cd ..

sudo -i -u ctf bash << EOF
cd real_hack
./ynetd -p 1337 ./real_hack
cd ..
EOF

