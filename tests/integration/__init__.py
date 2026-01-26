"""Integration tests package.

These tests require running services:
- QuestDB on localhost:9000 (HTTP) and localhost:9009 (ILP)

To run QuestDB: docker run -d --name questdb -p 9000:9000 -p 9009:9009 questdb/questdb

Skip these tests with: pytest tests/ --ignore=tests/integration/
"""
