from django.db import models

# Create your models here.
#staff details

class StaffDetails(models.Model):
    Employee_ID = models.BigIntegerField(primary_key = True)
    name = models.CharField(max_length = 50)

    GENDER_MALE = 'Male'
    GENDER_FEMALE = 'Female'
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.CharField(choices = GENDER_CHOICES, 
                              max_length= 30, blank = True)
    date_of_birth = models.DateField(auto_now = False, auto_now_add = False, blank = True)
    CID = models.CharField(max_length=11, unique=True, blank=True)

    Administration = 'Administration'
    TeachingStaff = 'Teaching Staff'
    NonTeachingStaff = 'Non Teaching Staff'
    SupportingStaff = 'Supporting Staff'
    Category_choices = [(Administration, 'Administration'), 
                        (TeachingStaff, 'TeachingStaff'), 
                        (NonTeachingStaff, 'Non Teaching Staff'),
                        (SupportingStaff, 'Supporting Staff')]
    
    category = models.Charfield(choices=Category_choices, max_length=30, 
                                blank=True)
    
    position_title = models.Charfield(max_length=50, blank=True)
    position_level = models.CharField(max_length=50, blank=True)
    grade = models.CharField(max_length=5, blank=True)
    appointment_date = models.Datefeld(auto_now=False, auto_now_add=False,
                                       blank=True)
    join_date = models.DateField(auto_now=False, auto_add_now = False,
                                 blank = True)
    transferred_from = models.CharField(max_length=30, blank=True)

    Regular = 'Regular'
    Contract = 'Contract'
    Employment_choices = [(Regular, 'Regular'), (Contract, 'Contract')]
    Employment_type=models.CharField(choices=Employment_choices, max_length=30,
                                     blank=True)
    
    Nationality = models.CharField(max_length=50, blank=True)
    Subject = models.CharField(max_length = 50, blank=True)
    Qualification = models.TextField(blank=True)
    Contact_number = models.CharField(max_length = 14, blank= True)
    Email = models.EmailField(blank=True, unique=True)
    permanent_address = models.TextField(blank=True)
    profile_pic =models.ImageField(upload_to="images/staff", default="/static/images/user.jpg", null=True, blank=True)


    def __str__(self):
        return '%s %s' %(self.name, self.position_title)
    

#Add Subject
    
class Subject(models.Model):
    subject = models.CharField(max_length = 100)

    def __str__(self):
        return self.subject
    

#Class Teacher
    
class ClassTeacher(models.Model):
    name = models.ForeignKey(StaffDetails, on_delete=models.CASCADE)

    one = '1'
    two = '2'
    three = '3'
    four = '4'
    five = '5'
    six = '6'
    seven = '7'
    eight = '8'
    nine = '9'
    

    class_choices = [(one, '1'),
                     (two, '2'), 
                     (three, '3'),
                     (four, '4'), (five, '5'), (six, '6'),
                     (seven, '7'), (eight, '8'), (nine, '9')]
    
    standard = models.CharField(choices=class_choices, max_length=30)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'
    G = 'G'
    H = 'H'
    I = 'I'

    section_choices = [(A, 'A'), (B, 'B'), (C, 'C'),
                       (D, 'D'), (E, 'E'), (F, 'F'), 
                       (G, 'G'),(H, 'H'),(I, 'I')]
    section = models.CharField(choices=section_choices, max_length=30)
    
    def __str__(self):
        return '%s' %(self.name)
    

#student details

class StudentDetail(models.Model):
    student_CODE = models.CharField(Max_length = 50, primary_key = True)
    name = models.CharField(max_length=50)

    GENDER_MALE = 'Male'
    GENDER_FEMALE = 'Female'
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.CharField(choices = GENDER_CHOICES, 
                              max_length= 30, blank = True)
    
    one = '1'
    two = '2'
    three = '3'
    four = '4'
    five = '5'
    six = '6'
    seven = '7'
    eight = '8'
    nine = '9'
    

    class_choices = [(one, '1'),
                     (two, '2'), 
                     (three, '3'),
                     (four, '4'), (five, '5'), (six, '6'),
                     (seven, '7'), (eight, '8'), (nine, '9')]
    
    standard = models.CharField(choices=class_choices, max_length=30)

    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'
    G = 'G'
    H = 'H'
    I = 'I'

    section_choices = [(A, 'A'), (B, 'B'), (C, 'C'),
                       (D, 'D'), (E, 'E'), (F, 'F'), 
                       (G, 'G'),(H, 'H'),(I, 'I')]
    section = models.CharField(choices=section_choices, max_length=30)

    subject = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)

    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    admission_no = models.BigIntegerField(blank=True)
    date_of_admission = models.DateField(auto_now = False, auto_now_add=False, blank = True)
    parent_email = models.EmailField(blank=True, unique=True)
    CID = models.CharField(max_length=11, unique=True, blank=True)
    class_teacher = models.ForeignKey(ClassTeacher, null=True, on_delete=models.SET_NULL)
    previous_school = models.TextField(blank=True)
    proctor_master = models.ForeignKey(StaffDetails, null=True, on_delete=models.SET_NULL)

    Boarder = 'Boarder'
    DayScholar = 'DayScholar'
    Scholar_choice = [(Boarder, 'Boarder'), 
                      (DayScholar, 'DayScholar')]
    Scholar_type = models.CharField(choices=Scholar_choice, blank=True, max_length=30)

    Regular = 'Regular'
    Repeater = 'Repeater'
    RegularOrRepeater = [(Regular, 'Regular'), (Repeater, 'Repeater')]
    RegularOrRepeater = models.CharField(choices=RegularOrRepeater, blank=True, max_length=30)

    profile_pic = models.Imagefield(upload_to="Images/students", default="/static/images/user.jpg", null=True, blank=True)
    fathers_name = models.CharField(max_length=50, blank=True)
    mothers_name = models.CharField(max_length=50, blank=True)
    parent_mobile_phone = models.CharField(max_length=14, blank=True)


    def __str__(self):
        return '%s %s %s' %(self.name, self.standard, self.section)
