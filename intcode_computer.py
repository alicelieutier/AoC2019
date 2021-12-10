def i_add(mem, p1, p2, p3, param_modes, i, **_):
  p1 = p1 if param_modes[0] == 1 else mem[p1]
  p2 = p2 if param_modes[1] == 1 else mem[p2]
  mem[p3] = p1 + p2
  return (mem, i + 4)

def i_multiply(mem, p1, p2, p3, param_modes, i, **_):
  p1 = p1 if param_modes[0] == 1 else mem[p1]
  p2 = p2 if param_modes[1] == 1 else mem[p2]
  mem[p3] = p1 * p2
  return (mem, i + 4)

def i_input(mem, p1, input, i, **_):
  mem[p1] = next(input)
  return (mem, i + 2)

def i_output(mem, p1, param_modes, i, output, **_):
  p1 = p1 if param_modes[0] == 1 else mem[p1]
  output.append(p1)
  return (mem, i + 2)

def i_jump_if_true(mem, p1, p2, param_modes, i, **_):
  p1 = p1 if param_modes[0] == 1 else mem[p1]
  p2 = p2 if param_modes[1] == 1 else mem[p2]
  if p1 != 0:
    return (mem, p2)
  return (mem, i + 3)

def i_jump_if_false(mem, p1, p2, param_modes, i, **_):
  p1 = p1 if param_modes[0] == 1 else mem[p1]
  p2 = p2 if param_modes[1] == 1 else mem[p2]
  if p1 == 0:
    return (mem, p2)
  return (mem, i + 3)

def i_less_than(mem, p1, p2, p3, param_modes, i, **_):
  p1 = p1 if param_modes[0] == 1 else mem[p1]
  p2 = p2 if param_modes[1] == 1 else mem[p2]
  mem[p3] = 1 if p1 < p2 else 0
  return (mem, i + 4)

def i_equals(mem, p1, p2, p3, param_modes, i, **_):
  p1 = p1 if param_modes[0] == 1 else mem[p1]
  p2 = p2 if param_modes[1] == 1 else mem[p2]
  mem[p3] = 1 if p1 == p2 else 0
  return (mem, i + 4)

opcodes = {
  1: (3, i_add),
  2: (3, i_multiply),
  3: (1, i_input),
  4: (1, i_output),
  5: (2, i_jump_if_true),
  6: (2, i_jump_if_false),
  7: (3, i_less_than),
  8: (3, i_equals),
  99: (0, lambda mem : mem), # remove?
}

# A position in memory is called an address
# Opcodes mark the beginning of an instruction.
# The values used immediately after an opcode,
#   if any, are called the instruction's parameters
# The address of the current instruction is called the instruction pointer
# After an instruction finishes, the instruction pointer increases by the number of values in the instruction

def parse_instruction(value):
  opcode = value % 100
  params_needed = opcodes[opcode][0]
  param_modes = [value // 10**i % 10 for i in range(2, 2 + params_needed)]
  return (opcode, tuple(param_modes))

def execute(state, input=[]):
  input_gen = (item for item in input)
  i = 0
  output = []
  while True:
    opcode, param_modes = parse_instruction(state[i])
    if opcode == 99: break
    param_needed, fun = opcodes[opcode]
    params = state[i + 1 : i + param_needed + 1]
    state, i = fun(state, *params, param_modes=param_modes, input=input_gen, i=i, output=output)
  return output

if __name__ == "__main__":
  assert execute([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], input=[4]) == [999]




