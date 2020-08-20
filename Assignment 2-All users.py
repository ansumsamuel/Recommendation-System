
print ()

import math
from operator import itemgetter

# definie class similarity
class similarity:
    
    # Class instantiation 
    def __init__ (self, ratingP, ratingQ):
        self.ratings1 = ratingP
        self.ratings2 = ratingQ

    # Minkowski Distance between two vectors
    def minkowski(self, r):
    
        # calcualte minkowski distance
        distance = 0       
        for k in (set(self.ratings1.keys()) & set(self.ratings2.keys())):
            p = self.ratings1[k]
            q = self.ratings2[k]
            distance += pow(abs(p - q), r)
    
        # return value of minkowski distance
        return pow(distance,1/r)

    # Pearson Correlation between two vectors
    def pearson(self):
        
        # Step 1.1
        # set n to the number of common keys
        # do not hardcode! 
        # this should work no matter which 2 dictionares I provide
        # YOUR CODE HERE
        n=0
        commonkeys=[]
        for k in self.ratings1.keys():
            if k in self.ratings2.keys():
                n=n+1
                commonkeys.append(k)
#        print (n)
            
        
        # Step 1.2
        # error check for n==0 condition, and
        # return -2 if n==0
        # YOUR CODE HERE
        if n==0:
            return -2
        else:
            
         
        # Step 1.3
        # use a SINGLE for loop to calculate the partial sums
        # in the computationally efficient form of the pearson correlation   
        # YOUR CODE HERE
            pq=0
            p=0
            q=0
            psq=0
            qsq=0
            for i in commonkeys:
                pq=pq+self.ratings1[i]*self.ratings2[i]
                p=p+self.ratings1[i]
                q=q+self.ratings2[i]
                psq=psq+pow(self.ratings1[i],2)
                qsq=qsq+pow(self.ratings2[i],2)
            pwsq=pow(p,2)
            qwsq=pow(q,2)
                
          
        # Step 1.4
        # calcualte the numerator term for pearson correlation
        # using relevant partial sums
        # YOUR CODE HERE
        num=pq-((p*q)/n)
        
        # Step 1.5
        # calcualte the denominator term for pearson correlation
        # using relevant partial sums
        # YOUR CODE HERE
        den=pow((psq-pwsq/n),1/2)*pow((qsq-qwsq/n),1/2)
        
        # Step 1.6
        # error check for denominator==0 condition
        # return -2 if denominator==0
        # YOUR CODE HERE
        if den==0:
            return -2
        else:

        # Step 1.7
        # calcualte the pearson correlation 
        # using the numerator and deonomminator
        # and return the pearson correlation
        # YOUR CODE HERE
            r=round(num/den,2)
            return(r)

# user ratings - this is the same data as we used in the User Recommendation Lecture
songData = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }

# for whom are we making recommendations?
#userX = "Veronica"
#userXRatings = songData[userX]
for userX in songData.keys():
    userXRatings = songData[userX]

# Step 2.1
# find the similarity measure (pearson correlation) between userX's ratings, and each of the other user's ratings.
# DO NOT include userX's similarity measure from userX.
# use a for loop to get at the other users and their ratings - DO NOT hard code.
# use the similarity class to caclulate the simialrity measure (pearson correlation) between user ratings.
# assign list of (user, similarityMeasure) tuples to a variable called userSimilarities.
# Example of how userSimilarities might look: [('Angelica', 0.42), ('Bill', 0.0), ('Chan', 0.5), ('Dan', 0.39), ('Jordyn', 0.61), ('Sam', -2), ('Veronica', -2)]
# YOUR CODE HERE
    userSimilarities=[]
    for user,userYRatings in songData.items():
       
    
        if user != userX:
        
           CallingClass=similarity(userXRatings,userYRatings)
           similarityMeasure=CallingClass.pearson()
           x=(user,similarityMeasure)
           userSimilarities.append(x)
# Step 2.2
# sort the list of tuples by highest simialrity to lowest similarity.
# assign the sorted list to a variable called sortedUserSimilarities.
# Example of how sortedUserSimilarities might look: [('Jordyn', 0.61), ('Chan', 0.5), ('Angelica', 0.42), ('Dan', 0.39), ('Bill', 0.0), ('Sam', -2), ('Veronica', -2)]
# YOUR CODE HERE

    from operator import itemgetter
    sortedUserSimilarities=sorted(userSimilarities,key=itemgetter(1),reverse= True)
#print(sort)

# Step 2.3
# userX's NN is the user at the 0th position of the sorted list.
# assign the NN to a variable called userXNN.
# Example of how userXNN might look: 'Jordyn'
# YOUR CODE HERE
    userXNN=sortedUserSimilarities[0][0]
#print(userXNN)

    

# Step 2.4
# recos for userX should include albums rated by userXNN, not already rated by userX.
# assign the list of (album, rating) tuples to a variable called userXRecos.
# Example of how userXRecos might look: [('Slightly Stoopid', 4.5), ('Phoenix', 5.0)]
# YOUR CODE HERE
    userXRecos=[]
    for album,rating in songData[userXNN].items():
      if album not in songData[userX].keys():
          tup=(album,rating)
          userXRecos.append(tup)

# Step 2.5
# sort list of tuples by highest rating to lowest rating.
# assign sorted list to a varaible userXSortedRecos.
# Example of how userXSortedRecos might look: [('Phoenix', 5.0), ('Slightly Stoopid', 4.5)]
# YOUR CODE HERE
    userXSortedRecos=sorted(userXRecos,key=itemgetter(1),reverse= True)

    print ("Recommendations for", userX,":",userXSortedRecos)
print ("--------------------------")
print ()
#print (userXSortedRecos)