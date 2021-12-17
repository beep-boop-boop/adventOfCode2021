import math as m
regs = [reg.strip() for reg in open('inputs/day17.txt').readline().split(':')[1].split(',')]

regs[0] = [int (num) for num in regs[0].replace('x=', '').split('..')]
regs[1] = [int (num) for num in regs[1].replace('y=', '').split('..')]


min_x_vel = m.ceil((-1 + ((8 * regs[0][0]) + 1) ** 0.5) / 2)
max_x_vel = regs[0][1] # an x velocity greater than that will make the probe overshoot after 1 time step

max_down_y_vel = regs[1][0] # more than that and the probe will overshoot in the downwards direction.
max_up_y_vel = abs(regs[1][0]) # when the probe is shot upwards with a vertical velocity of y, it comes back to the starting point with a vertical velocity of  -y - 1

max_peak_y = sum(range(max_up_y_vel))

velocities = 0

def validate(x_vel, y_vel):
    if y_vel >= 0:
        steps_to_zero = (2 * y_vel) + 1
        x_when_lands = 0
        vel = x_vel
        for _ in range(steps_to_zero):
            x_when_lands += vel
            if vel > 0:
                vel -= 1
            if vel == 0:
                vel = 0
        if (vel == 0) and (x_when_lands > regs[0][1] or x_when_lands < regs[0][0]):
            return False # does not reach the target horizontally
        elif (vel == 0) and (regs[0][0] <= x_when_lands <= regs[0][1]): # horizontal velocity runs out over target zone
            y_vel_when_landed = (-1 * y_vel) - 1
            y = 0
            while y >= regs[1][0]:
                y += y_vel_when_landed
                y_vel_when_landed -= 1
                if regs[1][0] <= y <= regs[1][1]:
                    return True
            return False
        else:
            x = x_when_lands
            y = 0
            y_vel_when_landed = (-1 * y_vel) - 1
            while y >= regs[1][0]:
                y += y_vel_when_landed
                y_vel_when_landed -= 1
                x += vel
                if vel > 0:
                    vel -= 1
                else:
                    vel = 0
                if regs[1][0] <= y <= regs[1][1] and regs[0][0] <= x <= regs[0][1]:
                    return True
            return False
    else:
        vel = x_vel
        x = 0
        y = 0
        while y >= regs[1][0]:
            y += y_vel
            y_vel -= 1
            x += vel
            if vel > 0:
                vel -= 1
            else:
                vel = 0
            if regs[1][0] <= y <= regs[1][1] and regs[0][0] <= x <= regs[0][1]:
                return True
        return False


for x_vel in range(min_x_vel, max_x_vel + 1):
    for y_vel in range(max_down_y_vel, max_up_y_vel + 1):
        if validate(x_vel, y_vel):
            velocities += 1


print(max_peak_y)
print(velocities)