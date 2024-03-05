#####################################################
# Return the minimum number of clips needed so that
# we can cut the clips into segments that cover the
# entire sporting event [0, time]. If the task is
# impossible, return -1.
#####################################################


# We currently know two techniques, two pointer and sliding window.
# I think sliding window works but I was unable to solve the problem with it.
# Two Pointers was easier to solve than sliding window.

def videoStitching(clips, time) -> int:
    clips.sort()  # Step 1: Sort the clips by their start times.

    curr_max, next_max = 0,0
    clips_used =  0

    while curr_max < time:
        for i in range(len(clips)):
            if clips[i][0] <= curr_max:
                next_max = max(next_max, clips[i][1])
                i += 1
            else: 
                break

        if curr_max == next_max:
            return -1

        curr_max = next_max
        clips_used += 1

    return clips_used
