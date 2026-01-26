Example `hello_world_server` is missing for `azmq`. Would you like to contribute it? Then follow the steps below:

```
    git clone https://github.com/zeromq/zeromq.org
    example_dir=content/docs/examples/cpp/azmq
    cd zeromq.org && mkdir -p $example_dir
    [ -s $example_dir/index.md ] || cat >$example_dir/index.md <<'EOF'
---
headless: true
---
EOF
    cp archetypes/examples/hello_world_server.md
    $example_dir/hello_world_server.md
```