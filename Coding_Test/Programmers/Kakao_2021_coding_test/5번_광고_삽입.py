# https://programmers.co.kr/learn/courses/30/lessons/72414
def make_sec(time):
    h,m,s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def make_time(sec):
    h = sec // 3600
    m = (sec % 3600) // 60
    s = sec % 60
    return f'{h:02d}:{m:02d}:{s:02d}'

def solution(play,adv,logs):
    play_sec = make_sec(play)
    sec_table = [0] * (play_sec + 1)

    # step 2
    for log in logs:
        start, end = log.split('-')
        sec_table[make_sec(start)] += 1
        sec_table[make_sec(end)] -= 1

    # step 3, 4
    for _ in range(2):
        for i in range(1, play_sec):
            sec_table[i] = sec_table[i] + sec_table[i-1]
    
    at = make_sec(adv)
    max_sec = 0
    max_i = 0

    for i in range(at - 1, play_sec):
        if i >= at:
            e = sec_table[i]
            f = sec_table[i - at]
            if max_sec < sec_table[i] - sec_table[i - at]:
                max_sec = sec_table[i] - sec_table[i - at]
                max_i = i
        else:
            if max_sec < sec_table[i]:
                max_sec = sec_table[i]
                max_i = i                  

    return make_time(max_i - at + 1)
  
'''
play_time	adv_time	    logs	                                                                                                    result
"02:03:55"	"00:14:15"	["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]	"01:30:59"
"99:59:59"	"25:00:00"	["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]	                    "01:00:00"
"50:00:00"	"50:00:00"	["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]	                                          "00:00:00"
'''
