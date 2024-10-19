<%@ include file="common/header.jspf" %>
<%@ include file="common/navigation.jspf" %>
<div class="container">
	<h1>Enter Task Details</h1>
	<form:form method="post" modelAttribute="task">
		<fieldset class="mb-3">
			<form:label path="description">Description</form:label>
			<form:input type="text" path="description" required="required"/>
			<form:errors path="description" cssClass="text-warning"/>
		</fieldset>
		
		<fieldset class="mb-3">
			<form:label path="dueDate">Due Date</form:label>
			<form:input type="text" path="dueDate" required="required"/>
			<form:errors path="dueDate" cssClass="text-warning"/>
		</fieldset>
		
		<form:input type="hidden" path="id"/>
		<form:input type="hidden" path="complete"/>
		<input type="submit" class="btn btn-success"/>
	</form:form>
</div>
<%@ include file="common/footer.jspf" %>
<script src="webjars/bootstrap-datepicker/1.9.0/js/bootstrap-datepicker.min.js"></script>
<script type="text/javascript">
	$('#dueDate').datepicker({
		format: 'yyyy-mm-dd'
	});
</script>



