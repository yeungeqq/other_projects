<%@ include file="common/header.jspf" %>
<%@ include file="common/navigation.jspf" %>
<div class="container">
	<h1>Open Tasks for ${name}</h1>
	<table class="table">
		<thead>
			<tr>
				<th>Description</th>
				<th>Due Date</th>
				<th>Complete</th>
			</tr>
		</thead>
		<tbody>
			<c:forEach items="${tasks}" var="task">
				<tr>
					<td>${task.description}</td>
					<td>${task.dueDate}</td>
					<td>${task.complete}</td>
					<td><a href="update-task?id=${task.id}" class="btn btn-warning">Update</a></td>
					<td><a href="delete-task?id=${task.id}" class="btn btn-danger">Delete</a></td>
					<td><a href="update-complete-task?id=${task.id}" class="btn btn-success">Mark as Complete</a></td>
				</tr>
			</c:forEach>
		</tbody>
	</table>
	<a href="add-task" class="btn btn-primary">Add Task</a>
</div>
<%@ include file="common/footer.jspf" %>