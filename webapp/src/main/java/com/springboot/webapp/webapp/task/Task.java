package com.springboot.webapp.webapp.task;

import java.time.LocalDate;

import jakarta.persistence.*;
import jakarta.validation.constraints.Size;

@Entity
public class Task {

	@Id
	@GeneratedValue
	private int id;
	
	private String username;
	
	@Size(min=1, message="Description cannot be empty")
	private String description;
	private LocalDate dueDate;
	private String complete;
	
	public Task() {};

	public Task(int id, String username, String description, LocalDate dueDate, String complete) {
		super();
		this.id = id;
		this.username = username;
		this.description = description;
		this.dueDate = dueDate;
		this.complete = complete;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getUsername() {
		return username;
	}

	public void setUsername(String username) {
		this.username = username;
	}

	public String getDescription() {
		return description;
	}

	public void setDescription(String description) {
		this.description = description;
	}

	public LocalDate getDueDate() {
		return dueDate;
	}

	public void setDueDate(LocalDate dueDate) {
		this.dueDate = dueDate;
	}

	public String getComplete() {
		return complete;
	}

	public void setComplete(String complete) {
		this.complete = complete;
	}

	@Override
	public String toString() {
		return "Task [id=" + id + ", username=" + username + ", description=" + description + ", dueDate="
				+ dueDate + ", complete=" + complete + "]";
	}

}
