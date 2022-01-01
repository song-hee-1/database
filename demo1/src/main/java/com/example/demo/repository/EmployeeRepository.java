package com.example.demo.repository;

import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.HashMap;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;


@Repository
public class EmployeeRepository {
	@Autowired
	private JdbcTemplate jdbcTemplate;
	public void SelectJdbc(JdbcTemplate jdbcTemplate) {
		    this.jdbcTemplate = jdbcTemplate;
		  }

	public ArrayList<HashMap<String, String>> getEmployees() {
		ArrayList<HashMap<String,String>> employeesList = new ArrayList<HashMap<String,String>>();
		String sql = "SELECT S.rating, AVG(S.age) as avgage FROM Sailors S WHERE S.age >= 18 GROUP BY S.rating HAVING COUNT(*) > 1";
		jdbcTemplate.query(sql,
				(ResultSet rs) -> {
				    HashMap<String,String> results = new HashMap<>();
				    while (rs.next()) {
				        results.put("rating = " + rs.getString(1) + " ", " avgage = " + rs.getString(2) + " ");
				        
				    }

				    employeesList.add(results);
				    return results;
				 	
	});
		   return employeesList;
	}
}
