package com.springboot.webapp.webapp.task;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;

public interface TaskRepo extends JpaRepository<Task, Integer>{
	public List<Task> findByUsername(String username);
}
