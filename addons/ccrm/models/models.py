# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Student(models.Model):
	_name ='student.personal.details'
	_description='Student  Detail'

	name=fields.Char(required=True,index=True,translate=True)
	display_name = fields.Char(store=True, index=True)
	email = fields.Char()
	postal_address=fields.Char()
	personal_address=fields.Char()
	dob = fields.Date(index=True)
	en_no=fields.Char()
	pass_out_year=fields.Char()
	pincode=fields.Char()
	ten_percentage=fields.Char()
	tweleve_percentage=fields.Char()
	spi=fields.Char()
	cpi=fields.Char()
	area_of_interest=fields.Char()
	mobile_no=fields.Char()
	father_name=fields.Char()
	father_occupation=fields.Char()
	mother_name=fields.Char()
	mother_occupation=fields.Char()
	father_contact=fields.Char()
	total_income=fields.Char()
	carrier_option=fields.Selection([
	('job','Job'),
	('higher study','Higher Study')],string='Carrier_Option',required=True,copy=False,default='job')
	branch=fields.Selection([
	('computer','Computer'),
	('electrical','Electrical'),
	('mechanical','Mechanical'),
	('civil','Civil')],string='Branch',required=True,copy=False,default='computer')
	course=fields.Selection([
	('b.e','B.E'),
	('m.e','M.E'),
	('diploma','Diploma')],string='Course',required=True,copy=False,default='b.e')
	city=fields.Selection([
	('mehsana','Mehsana'),
	('ahemdabad','Ahemadabad'),
	('ghandhinagar','Ghandhinagar'),
	('siddhpur','Siddhpur')],string='City',required=True,copy=False,default='mehsana')
	state=fields.Selection([
	('gujarat','Gujarat'),
	('rajsthan','Rajsthan'),
	('goa','Goa'),
	('delhi','Delhi')],string='State',required=True,copy=False,default='gujarat')
	district=fields.Selection([
	('mehsana','Mehsana'),
	('ahemdabad','Ahemadabad'),
	('ghandhinagar','Ghandhinagar'),
	('siddhpur','Siddhpur')],string='District',required=True,copy=False,default='mehsana')
	gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')], string='Gender', required=True, copy=False, default='female')

	image=fields.Binary("image")


class Company(models.Model):
	_name='company.details'
	_description='Company Detail'

	name=fields.Char()
	company_name=fields.Char()
	contact_person=fields.Char()
	designation=fields.Char()
	email=fields.Char()
	hr_name=fields.Char()
	mobile_no=fields.Char()
	address=fields.Char()
	location=fields.Char()
	email_hr=fields.Char()
	remarks=fields.Char()
	image=fields.Binary("image")
