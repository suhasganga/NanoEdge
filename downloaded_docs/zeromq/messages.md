Example `messages_strings_send_recv` is missing for `zmqpp`. Would you like to contribute it? Then follow the steps below:

```
    git clone https://github.com/zeromq/zeromq.org
    example_dir=content/docs/examples/cpp/zmqpp
    cd zeromq.org && mkdir -p $example_dir
    [ -s $example_dir/index.md ] || cat >$example_dir/index.md <<'EOF'
---
headless: true
---
EOF
    cp archetypes/examples/messages_strings_send_recv.md
    $example_dir/messages_strings_send_recv.md
```