# Problem: Bat programmer in Arkham City needs to help BatMan capture asylum escapees

**"Elizabeth Arkham Asylum for the Criminally Insane"** is a hospital for patients who are insane and commit criminal acts. It is famous for its evil practices. Today one of the doctors wanted to perform a group hypnosis experiment. On the other side of the city, some bad people plan to rob a bank and blow up the city's power supply right in the middle of the hypnosis session. During that blackout, some people escaped and started walking in every direction. Because they are all hypnotic and the doctor who engaged them gave some suggestions before the outage, they can walk only in a specific pattern.

## Walking Pattern:

Patient ten takes ten steps in the time requiring patient one to take one step. Patient five takes five steps in the same time requiring patient one to take one step. So, patient ten can take two steps in the time requiring patient five can take one step.

## Task:

In your job as a Bat programmer, you need to write a function/method to find out how many steps it requires for Batman to tag every so Asylum staff can pick them up. Tagging involves reaching the patient and returning to the asylum to hand over the tag injector and pick up a new one. Assume Batman can run at infinite steps in the time requiring the patient one to take one step. In other words, he can tag all the patients in the same instance but must make it to each patient.

## Input:

You will get the number of patients who escaped and at what step of the first patient Batman started.

## Example:

findNumOfStepsRequired(3, 10)
returns 30

## Explanation:

After ten steps patient one is 10 steps away from the asylum.
After ten steps of patient one, patient two is 20 steps away from the asylum.
After ten steps of patient one, patient three is 30 steps away from the asylum.
