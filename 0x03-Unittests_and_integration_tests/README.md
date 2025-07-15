0x03-Unittests_and_integration_tests

- Mocking, parametrization, and fixtures are patterns to test the code
  1 - Mocking: replacing dependencies wiht cntrolled objects that mimic their behavior.
  (fast & better to isolate the unit being tested)
  2 - parametrization: runs the same test cade with diffferent input.
  (reduced redundeancy & easier maintenace of test cases)
  3 - fixtures: setup a consistent environment for tests, used to fet datea ready. it run vefor "setup" and sometime after "teardown" the test function.
  (improve test orfanization & better test isolation)
