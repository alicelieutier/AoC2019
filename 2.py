def process(memory):
    for i in range(0, len(memory), 4):
        opcode = memory[i]
        if opcode == 99:
            return memory
        pos1 = memory[i + 1]
        pos2 = memory[i + 2]
        dest = memory[i + 3]
        if opcode == 1:
            memory[dest] = memory[pos1] + memory[pos2]
        if opcode == 2:
            memory[dest] = memory[pos1] * memory[pos2]
    return memory

def find_noun_and_verb(program):
    for noun in range(0, 100):
        for verb in range(0, 100):
            memory = list(program)
            memory[1] = noun
            memory[2] = verb
            if process(memory)[0] == 19690720:
                return noun, verb

if __name__ == "__main__":
    # part 1 tests 
    assert(process([1,0,0,0,99]) == [2,0,0,0,99])
    assert(process([2,3,0,3,99]) == [2,3,0,6,99])
    assert(process([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99])
    assert(process([2,4,4,5,99,0]) == [2,4,4,5,99,9801])
    assert(process([1,9,10,3,2,3,11,0,99,30,40,50]) == [3500,9,10,70,2,3,11,0,99,30,40,50])
    assert(process([]) == [])

    gravity_assist_program = (1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,10,23,2,10,23,27,1,27,6,31,1,13,31,35,1,13,35,39,1,39,10,43,2,43,13,47,1,47,9,51,2,51,13,55,1,5,55,59,2,59,9,63,1,13,63,67,2,13,67,71,1,71,5,75,2,75,13,79,1,79,6,83,1,83,5,87,2,87,6,91,1,5,91,95,1,95,13,99,2,99,6,103,1,5,103,107,1,107,9,111,2,6,111,115,1,5,115,119,1,119,2,123,1,6,123,0,99,2,14,0,0)
    memory = list(gravity_assist_program)
    memory[1] = 12
    memory[2] = 2
    print(process(memory)[0])

    # part 2
    noun, verb = find_noun_and_verb(gravity_assist_program)
    print('noun:{}, verb:{}'.format(noun, verb))
    print(100 * noun + verb)

