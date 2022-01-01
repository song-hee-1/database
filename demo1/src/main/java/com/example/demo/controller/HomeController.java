package com.example.demo.controller;
 
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.repository.EmployeeRepository;


@RestController
public class HomeController {
    
	/*
	@RequestMapping(value="/")
	public String index() {
	    
	    return "index";
	}
	*/
	
	
	
	  @Autowired
	  EmployeeRepository employeeRepository;


	
	@RequestMapping(value="/employee") //http://localhost:8000/employee
	 public ArrayList<HashMap<String, String>> getEmployees() 
	    {
		  return employeeRepository.getEmployees();
		
	    }


}
