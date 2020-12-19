import random
test = input('Enter AMC test you want.')
problemnum=int(input('Starting problem number?'))
list1=['A','B']
correct = 'yes'
while True:
  if test == '10' or test == '12':
    print ('artofproblemsolving.com/wiki/index.php/'+str(random.randint(2002,2020))+'_AMC_'+str(test)+str(random.choice(list1))+'_Problems/Problem_'+str(problemnum))
  else:
    print ('fail')
  if test == '8':
     print ('artofproblemsolving.com/wiki/index.php/'+str(random.randint(2002,2020))+'_AMC_'+str(test)+'_Problems/Problem_'+str(problemnum))
  correct = input('Correct? Enter yes or no.')
  if correct == 'yes':
    if problemnum<25:
      problemnum+=1
  else:
    if problemnum>1:
      problemnum-=1