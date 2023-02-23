import time

import pigpio

GPIO = 23
FREQ = 38.0
GAP_S = 0.1
OFF_CMD = [3378, 1641, 439, 1242, 439, 398, 439, 398, 439, 398, 439, 398, 439, 398, 439, 398, 439, 398, 439, 398, 439, 398,
           439, 398, 439, 398, 439, 1242, 439, 398, 439, 398, 439, 398, 439, 398, 439, 398, 439, 398, 439, 398, 439, 398,
           439, 398, 439, 398, 439, 398, 439, 398, 439, 398, 439, 398, 439, 398, 439, 398, 439, 398, 439, 1242, 439, 398,
           439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 398, 439, 1242, 439, 1242, 439, 1242,
           439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 398, 439, 398, 439, 398, 439, 398, 439,
           398, 439, 398, 439, 398, 439, 398, 439, 398, 439, 398, 439, 1242, 439, 1242, 439, 398, 439, 398, 439, 1242, 439,
           1242, 439, 1242, 439, 1242, 439, 398, 439, 398, 439, 1242, 439, 1242, 439, 398, 439, 398, 439, 398, 439, 398,
           439, 398, 439, 1242, 439, 1242, 439, 398, 439, 398, 439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 398, 439,
           398, 439, 1242, 439, 1242, 439, 398, 439, 1242, 439, 1242, 439, 398, 439, 398, 439, 1242, 439, 398, 439, 398,
           439, 398, 439, 398, 439, 398, 439, 1242, 439, 1242, 439, 398, 439, 1242, 439, 1242, 439, 1242, 439, 398, 439,
           398, 439, 398, 439, 398, 439, 398, 439, 1242, 439, 1242, 439, 398, 439, 1242, 439, 1242, 439, 1242, 439, 1242,
           439, 1242, 439, 398, 439, 398, 439, 1242, 439, 398, 439, 398, 439, 398, 439, 398, 439, 398, 439, 398, 439, 398,
           439, 398, 439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 398, 439,
           398, 439, 398, 439, 398, 439, 398, 439, 398, 439, 398, 439, 398, 439, 1242, 439, 1242, 439, 1242, 439, 1242,
           439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 398, 439, 398, 439, 398, 439, 398, 439, 398, 439, 398, 439,
           398, 439, 398, 439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 398,
           439, 398, 439, 398, 439, 398, 439, 398, 439, 398, 439, 398, 439, 398, 439, 1242, 439, 1242, 439, 1242, 439,
           1242, 439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 398, 439, 398, 439, 398, 439, 398, 439, 398, 439, 398,
           439, 398, 439, 398, 439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 1242, 439,
           1242, 439, 398, 439, 1242, 439, 398, 439, 1242, 439, 398, 439, 398, 439, 398, 439, 398, 439, 1242, 439, 398,
           439, 1242, 439, 398, 439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 398, 439, 398, 439, 398, 439, 398, 439,
           398, 439, 1242, 439, 1242, 439, 398, 439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 398, 439, 398,
           439, 398, 439, 398, 439, 398, 439, 398, 439, 398, 439, 398, 439, 398, 439, 398, 439, 1242, 439, 1242, 439, 1242,
           439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 398, 439, 398, 439, 398, 439, 398, 439, 398, 439,
           398, 439, 398, 439, 398, 439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 1242, 439, 1242,
           439]

SIGNAL_PREFIX = [3378, 1641]
BIT_ONE = [439, 1242]
BIT_ZERO= [439, 398]
SIGNAL_SUFIX=[439, ]

SET_TEMP_BIT_PREFIX =[[1, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 1, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 1, 0],
                      [1, 1, 1, 1, 1, 1, 0, 1],
                      [1, 1, 1, 1, 1, 1, 1, 1],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 1, 1, 0, 0, 1, 1],
                      [1, 1, 0, 0, 1, 1, 0, 0],
                      [0, 0, 0, 1, 1, 0, 0, 1],
                      [1, 1, 1, 0, 0, 1, 1, 0],
                      [0, 0, 1, 0, 0, 0, 1, 0],
                      [1, 1, 0, 1, 1, 1, 0, 1], ]

SET_TEMP_BIT_SUFFIX = [[0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 1, 1, 1, 1, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 1, 1, 1, 1, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 1, 1, 1, 1, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 1, 1, 1, 1, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 0, 1, 0, 1, 0, 0, 0],
                       [0, 1, 0, 1, 0, 1, 1, 1],
                       [1, 0, 0, 0, 1, 0, 1, 1],
                       [0, 1, 1, 1, 0, 1, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 1, 1, 1, 1, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 1, 1, 1, 1, 1, 1, 1]]


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def get_wave_from_bit_str(bit_string):
    wave = SIGNAL_PREFIX
    for bit in bit_string:
        if bit == '1':
            wave+=BIT_ONE
        else:
            wave+=BIT_ZERO
    wave+=SIGNAL_SUFIX
    return wave


def carrier(gpio, frequency, micros):
   """
   Generate carrier square wave.
   """
   wf = []
   cycle = 1000.0 / frequency
   cycles = int(round(micros/cycle))
   on = int(round(cycle / 2.0))
   sofar = 0
   for c in range(cycles):
      target = int(round((c+1)*cycle))
      sofar += on
      off = target - sofar
      sofar += off
      wf.append(pigpio.pulse(1<<gpio, 0, on))
      wf.append(pigpio.pulse(0, 1<<gpio, off))
   return wf


def send_command_to_ac(code):
    # create pi interface
    pi = pigpio.pi()
    pi.set_mode(GPIO, pigpio.OUTPUT)  # IR TX connected to this GPIO.
    pi.wave_add_new()

    emit_time = time.time()

    # Create wave
    marks_wid = {}
    spaces_wid = {}

    wave = [0] * len(code)

    for i in range(0, len(code)):
        ci = code[i]
        if i & 1:  # Space
            if ci not in spaces_wid:
                pi.wave_add_generic([pigpio.pulse(0, 0, ci)])
                spaces_wid[ci] = pi.wave_create()
            wave[i] = spaces_wid[ci]
        else:  # Mark
            if ci not in marks_wid:
                wf = carrier(GPIO, FREQ, ci)
                pi.wave_add_generic(wf)
                marks_wid[ci] = pi.wave_create()
            wave[i] = marks_wid[ci]

    delay = emit_time - time.time()

    if delay > 0.0:
        time.sleep(delay)

    pi.wave_chain(wave)

    while pi.wave_tx_busy():
        time.sleep(0.002)

    for i in marks_wid:
        pi.wave_delete(marks_wid[i])

    for i in spaces_wid:
        pi.wave_delete(spaces_wid[i])


def get_bit_codes_for_temp(temp):
    temp_bin = format(temp, '06b')
    temp_bin_str = ('00'+temp_bin[::-1])
    inv_temp_bin_str = ''.join('1' if x == '0' else '0' for x in temp_bin_str)
    return [temp_bin_str, inv_temp_bin_str]


def get_set_temp_bit_command(temp):
    set_temp_bit_command = SET_TEMP_BIT_PREFIX
    temperature_bit_code, inv_temperature_bit_code = get_bit_codes_for_temp(temp)
    set_temp_bit_command +=temperature_bit_code
    set_temp_bit_command += inv_temperature_bit_code
    set_temp_bit_command +=SET_TEMP_BIT_SUFFIX
    final_cmd =''
    for byte in set_temp_bit_command:
        for bit in byte:
            final_cmd += str(bit)
    return final_cmd


# send_command_to_ac(on_command)
# time.sleep(3)
# send_command_to_ac(off_command)

# wave_str = get_wave_from_bit_str(sample_bit_str)
# send_command_to_ac(wave_str)

# segments = list(chunks(sample_bit_str1, 8))
# for i, segment in enumerate(segments):
#     print i, segment
    # print i, int(''.join([str(x) for x in segment[::-1]]) ,2)
    # print(''.join(reversed(segments)))

cmd = get_wave_from_bit_str(get_set_temp_bit_command(20))
send_command_to_ac(cmd)
# time.sleep(3)

# send_command_to_ac(OFF_CMD)

# cmd_20 = get_wave_from_bit_str(get_set_temp_bit_command(20))
# send_command_to_ac(cmd_20)
print("that's all folks")
