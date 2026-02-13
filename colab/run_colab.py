!git clone https://github.com/<YOUR_USERNAME>/Job-Assignment-and-Scheduling-Optimization.git
%cd Job-Assignment-and-Scheduling-Optimization

!pip -q install -r requirements.txt

!python src/job_assignment_with_learning.py --data data/Process_Dataset.xlsx --sheet "Part 1"
