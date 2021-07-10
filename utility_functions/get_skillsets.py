job_skills = []
skillset = job_details.find('ul', 'skillslist').find_all('li')
for a_skill in skillset:
    job_skills.append(a_skill.text)