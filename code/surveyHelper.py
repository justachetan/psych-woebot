import matplotlib.pyplot as plt
import numpy as np

def prep_vol_array(fname):
    f = open(fname)
    counter = 0
    a = []
    for line in f:
        if counter == 0:
            counter+=1
            continue
        a.append(line.split(",")[1])
    return a


def calc_PHQ9_score(fname):
    fh = open(fname)
    counter = 0
    score_arr = []

    for line in fh:
        if(counter==0):
            counter+=1
            continue
        else:
            score = 0
            a = line.split(",")[2:11]
            for i in a:
                s = i.split(":")
                k = int(s[0].strip())
                score+=k
            score_arr.append(score)
    return score_arr

def calc_PHQ9_score_IIITD(fname):
    fh = open(fname)
    counter = 0
    score_arr = []
    
    for line in fh:
        if(counter<11):
            if(counter==0):
                counter+=1
                continue
            else:
                score = 0
                a = line.split(",")[2:11]
                for i in a:
                    s = i.split(":")
                    k = int(s[0].strip())
                    score+=k
                score_arr.append(score)
                counter+=1
    return score_arr

def calc_PHQ9_score_nonIIITD(fname):
    fh = open(fname)
    counter = 0
    score_arr = []
    
    for line in fh:
        if(counter>=11):
            if(counter==0):
                counter+=1
                continue
            else:
                score = 0
                a = line.split(",")[2:11]
                for i in a:
                    s = i.split(":")
                    k = int(s[0].strip())
                    score+=k
                score_arr.append(score)
                counter+=1
        else:
            counter+=1
    return score_arr



def create_PHQ9_plotpoints(score_array):

    plot_arr = [0]*5
    for i in score_array:

        if i >= 0 and i <=4:
            plot_arr[0]+=1
        elif i>=5 and i<=9:
            plot_arr[1]+=1
        elif i>=10 and i<=15:
            plot_arr[2]+=1
        elif i>=16 and i<=19:
            plot_arr[3]+=1
        elif i>=20 and i<=27:
            plot_arr[4]+=1

    return plot_arr


def render_score_pieplot_PHQ9(plot_array):
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    fig1, ax1 = plt.subplots()
    PHS_DEPRESSION_LEVEL_ARR = "None", "Mild", "Moderate", "Moderately severe", "Severe"
    ax1.pie(plot_array, labels=PHS_DEPRESSION_LEVEL_ARR, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title("Division of people on the basis of PHQ-9 Graded Responses")

    plt.show()
    
def render_score_pieplot_PHQ9_IIITD(plot_array):
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    fig1, ax1 = plt.subplots()
    PHS_DEPRESSION_LEVEL_ARR = "None", "Mild", "Moderate", "Moderately severe", "Severe"
    ax1.pie(plot_array, labels=PHS_DEPRESSION_LEVEL_ARR, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title("Division of people on the basis of PHQ-9 Graded Responses (IIITD)")

    plt.show()
    
def render_score_pieplot_PHQ9_nonIIITD(plot_array):
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    fig1, ax1 = plt.subplots()
    PHS_DEPRESSION_LEVEL_ARR = "None", "Mild", "Moderate", "Moderately severe", "Severe"
    ax1.pie(plot_array, labels=PHS_DEPRESSION_LEVEL_ARR, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title("Division of people on the basis of PHQ-9 Graded Responses (Non-IIITD)")

    plt.show()

def obtain_PANAS_positive(fname, num):

    fh = open(fname)
    counter = 0
    positive_score = 0
    for line in fh:
        if counter == 0:
            counter+=1
            continue
        else:
            cols = line.split(",")
            req_cols = cols[12:33]
            for j in req_cols:
                if(req_cols.index(j)%2==1):
                    positive_score+=int(j.split(":")[0].strip())

    return positive_score/num

def obtain_PANAS_positive_IIITD(fname, num):

    fh = open(fname)
    counter = 0
    positive_score = 0
    for line in fh:
        if(counter<11):
            if counter == 0:
                counter+=1
                continue
            else:
                cols = line.split(",")
                req_cols = cols[12:33]
                for j in req_cols:
                    if(req_cols.index(j)%2==1):
                        positive_score+=int(j.split(":")[0].strip())

    return positive_score/num

def obtain_PANAS_positive_nonIIITD(fname, num):

    fh = open(fname)
    counter = 0
    positive_score = 0
    for line in fh:
        if(counter>=11):
            if counter == 0:
                counter+=1
                continue
            else:
                cols = line.split(",")
                req_cols = cols[12:33]
                for j in req_cols:
                    if(req_cols.index(j)%2==1):
                        positive_score+=int(j.split(":")[0].strip())

    return positive_score/num



def render_PANAS_positive(fname_pre, fname_mid, fname_end):

    pre = obtain_PANAS_positive(fname_pre, 20)
    mid = obtain_PANAS_positive(fname_mid, 18)
    end = obtain_PANAS_positive(fname_end, 18)

    objects = ('Pre-Therapy', 'Mid-Therapy', 'End-Therapy')
    y_pos = np.arange(len(objects))
    performance = [pre, mid, end]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Positive-Effect Score')
    plt.title('Survey')

    plt.show()
    
def render_PANAS_positive_IIITD(fname_pre, fname_mid, fname_end):

    pre = obtain_PANAS_positive(fname_pre, 10)
    mid = obtain_PANAS_positive(fname_mid, 10)
    end = obtain_PANAS_positive(fname_end, 10)

    objects = ('Pre-Therapy', 'Mid-Therapy', 'End-Therapy')
    y_pos = np.arange(len(objects))
    performance = [pre, mid, end]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Positive-Effect Score (IIITD)')
    plt.title('Survey')

    plt.show()
    
def render_PANAS_positive_nonIIITD(fname_pre, fname_mid, fname_end):

    pre = obtain_PANAS_positive(fname_pre, 10)
    mid = obtain_PANAS_positive(fname_mid, 8)
    end = obtain_PANAS_positive(fname_end, 8)

    objects = ('Pre-Therapy', 'Mid-Therapy', 'End-Therapy')
    y_pos = np.arange(len(objects))
    performance = [pre, mid, end]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Positive-Effect Score (Non-IIITD)')
    plt.title('Survey')

    plt.show()

def obtain_PANAS_negative(fname, num):

    fh = open(fname)
    counter = 0
    positive_score = 0
    for line in fh:
        if counter == 0:
            counter+=1
            continue
        else:
            cols = line.split(",")
            req_cols = cols[12:33]
            for j in req_cols:
                if(req_cols.index(j)%2==0):
                    positive_score+=int(j.split(":")[0].strip())

    return positive_score/num

def obtain_PANAS_negative_IIITD(fname, num):

    fh = open(fname)
    counter = 0
    positive_score = 0
    for line in fh:
        if counter<11:
            if counter == 0:
                counter+=1
                continue
            else:
                cols = line.split(",")
                req_cols = cols[12:33]
                for j in req_cols:
                    if(req_cols.index(j)%2==0):
                        positive_score+=int(j.split(":")[0].strip())
                counter+=1

    return positive_score/num

def obtain_PANAS_negative_nonIIITD(fname, num):

    fh = open(fname)
    counter = 0
    positive_score = 0
    for line in fh:
        if counter>=11:
            if counter == 0:
                counter+=1
                continue
            else:
                cols = line.split(",")
                req_cols = cols[12:33]
                for j in req_cols:
                    if(req_cols.index(j)%2==0):
                        positive_score+=int(j.split(":")[0].strip())
                counter+=1
        else:
            counter+=1

    return positive_score/num


def render_PANAS_negative(fname_pre, fname_mid, fname_end):

    pre = obtain_PANAS_negative(fname_pre, 20)
    mid = obtain_PANAS_negative(fname_mid, 18)
    end = obtain_PANAS_negative(fname_end, 18)

    objects = ('Pre-Therapy', 'Mid-Therapy', 'End-Therapy')
    y_pos = np.arange(len(objects))
    performance = [pre, mid, end]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Negative-Effect Score')
    plt.title('Survey')

    plt.show()
    
def render_PANAS_negative_IIITD(fname_pre, fname_mid, fname_end):

    pre = obtain_PANAS_negative(fname_pre, 10)
    mid = obtain_PANAS_negative(fname_mid, 10)
    end = obtain_PANAS_negative(fname_end, 10)

    objects = ('Pre-Therapy', 'Mid-Therapy', 'End-Therapy')
    y_pos = np.arange(len(objects))
    performance = [pre, mid, end]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Negative-Effect Score (IIITD)')
    plt.title('Survey')

    plt.show()
    
def render_PANAS_negative_nonIIITD(fname_pre, fname_mid, fname_end):

    pre = obtain_PANAS_negative(fname_pre, 10)
    mid = obtain_PANAS_negative(fname_mid, 8)
    end = obtain_PANAS_negative(fname_end, 8)

    objects = ('Pre-Therapy', 'Mid-Therapy', 'End-Therapy')
    y_pos = np.arange(len(objects))
    performance = [pre, mid, end]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Negative-Effect Score (Non-IIITD)')
    plt.title('Survey')

    plt.show()
    
def obtain_PHQ9_ungraded(fname):
    fh = open(fname)
    score_arr = [0]*4
    counter = 0
    for line in fh:
        if counter==0:
            counter+=1
            continue
        cols = line.split(",")
        data = cols[11]
        if data.strip() == "Not difficult a tall":
            score_arr[0]+=1
        elif data.strip() == "Somewhat difficult":
            score_arr[1]+=1
        elif data.strip() == "Very difficult":
            score_arr[2]+=1
        else:
            score_arr[3]+=1
            
    return score_arr

def render_PHQ9_ungraded(score_arr):
    
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:

    fig1, ax1 = plt.subplots()
    PHS_UNGRADED = "Not difficult at all", "Somewhat difficult", "Very difficult", "Extremely difficult"
    ax1.pie(score_arr, labels=PHS_UNGRADED, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title("Division of people on the basis of PHQ-9 Ungraded Responses")
    plt.show()



if __name__ == '__main__':
    main()
