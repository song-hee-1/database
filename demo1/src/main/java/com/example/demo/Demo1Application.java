package com.example.demo;

import java.util.Arrays;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.security.servlet.SecurityAutoConfiguration;
import org.springframework.context.ApplicationContext;
import org.springframework.jdbc.core.JdbcTemplate;

@SpringBootApplication (exclude = SecurityAutoConfiguration.class)
public class Demo1Application {


	
	public static void main(String[] args) {
		 ApplicationContext ctx = SpringApplication.run(Demo1Application.class, args);
	
		 String[] beanNames = ctx.getBeanDefinitionNames();
         
	        Arrays.sort(beanNames);
	         
	        for (String beanName : beanNames) 
	        {
	            System.out.println(beanName);
	        }
	}



}
