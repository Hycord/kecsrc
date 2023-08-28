#!/usr/bin/env python3 


# get scores from the user 
scoreCount = 3


# display a title
print("The Test Scores program") 
print()

print(f"Enter {scoreCount} test scores") 
print("======================")


scores = [int(input("Enter test score: ")) for i in range(scoreCount)]

total_score = sum(scores)

# calculate average score 
average_score = round(total_score / scoreCount)

# map scores to string and join with space
score_string = " ".join(map(str, scores))

print("======================")
print(f"Your Scores: {score_string}")
print("Total Score: ", total_score, "\nAverage Score:", average_score)


print() 
print("Bye!")