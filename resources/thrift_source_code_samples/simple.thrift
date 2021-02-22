namespace c_glib TTest

// Presence of namespaces and sub-namespaces for which there is
// no generator should compile with warnings only
namespace noexist ThriftTest
namespace cpp.noexist ThriftTest

namespace * thrift.test

/**
 * Docstring!
 */
enum Numberz
{
  ONE = 1,
  TWO,
  THREE,
  FIVE = 5,
  SIX,
  EIGHT = 8
}

const Numberz myNumberz = Numberz.ONE;
