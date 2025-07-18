import * as bootstrap from 'bootstrap';
window.bootstrap = bootstrap;

/* Field Validation */
	function fieldValidation () {
		//HTML Elements
		let day = document.getElementById('day')

		if (day.value <=0 || day.value >31) {
			console.log('Invalid date') /*debug*/
			showModal('Invalid date', 'Please enter a valid date number', 'Close')
			day.value = ''
		}
	}


/* Clear Fields Function*/
	function clearFields(set = false) {
		//HTML Elements
		let year = document.getElementById('year')
		let month = document.getElementById('month')
		let day = document.getElementById('day')
		let type = document.getElementById('type')
		let desc = document.getElementById('desc')
		let exvalue = document.getElementById('exvalue')

		if (set == false) {
			year.value = ""
			month.value = ""
			day.value = ""
			type.value = ""
			desc.value = ""
			exvalue.value = ""
		} else {
			year.value = ""
			month.value = ""
			day.value = ""
			type.value = ""
			desc.value = ""
			exvalue.value = ""

			loadList()
		}
	}


/* Modal Wrap */
	let modalWrap = null;

	const showModal = (title, description, btn, status='error') => {
		//garbage collector
		if (modalWrap != null) {
			modalWrap.remove();
		}
		// HTML structure
		modalWrap = document.createElement('div');
		modalWrap.innerHTML = `
			<div id="modal" class="modal fade" tabindex="-1" aria-labelledby="modalLabel" aria-hidden="true">
				<div class="modal-dialog modal-dialog-centered">
					<div class="modal-content">
						<div class="modal-header" id="modalHeader">
							<h5 class="modal-title" id="titleLabel">${title}</h5>
							<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
						</div>
						<div class="modal-body" id="modal_content">
							${description}
						</div>

						<div class="modal-footer">
							<button type="button" class="btn" id="btnLabel" data-bs-dismiss="modal">${btn}</button>
						</div>
					</div>
				</div>
			</div>
		`;

		document.body.append(modalWrap);

		//	Modal style
		if (status == 'success') {
			document.getElementById('modalHeader').className += " text-success"
			document.getElementById('btnLabel').className += " btn-success"
		} else if(status == 'ok') { //Expense Removed
			document.getElementById('btnLabel').className += " btn-success"
		} else {
			document.getElementById('modalHeader').className += " text-danger"
			document.getElementById('btnLabel').className += " btn-danger"
		}

		var modal = new bootstrap.Modal(modalWrap.querySelector('.modal'));
		modal.show();
	}


/* Adding new Expenses Info */

	class Expense {
		constructor(year, month, day, type, desc, exvalue){
			this.year = year
			this.month = month
			this.day = day
			this.type = type
			this.desc = desc
			this.exvalue = exvalue
		}

		// keys validation
		dataValidation(){
			for(let i in this) {
				if (this[i] == undefined || this[i] == '' || this[i] == null) {
					return false
				}
			}
			return true
		}
	}

/* DataBank info control */
	class Db {
		constructor(){
			let id = localStorage.getItem('id')

			if (id === null) {
				localStorage.setItem('id', 0)
			}
		}

		getNextId(){
			let nextId = localStorage.getItem('id')
			
			return parseInt(nextId) + 1
		}

		//record expenses method
		record(e){
			let id = this.getNextId();
			localStorage.setItem(id, JSON.stringify(e));

			localStorage.setItem('id', id);

			// console.log(id) /*debug*/
		}

		getAll() {
			let id = localStorage.getItem('id')
			let expList = Array()

			for(let i = 1; i <= id; i++){
				let expense = JSON.parse(localStorage.getItem(i))
				//	console.log(i, expense) /*debug*/

				//if have ids removed
				if (expense == null) {
					continue	//jump
				}

				expense.id = i
				expList.push(expense)
			}
			//	console.log(expList) /*debug*/
			return expList
		}

		search(fields) {
			let filtered = Array()
			filtered = this.getAll()	//localStorage don't have a filer method
			//console.log(filtered) /*before - debug*/

			//year
			if (fields.year != '') {
				filtered = filtered.filter(i => i.year == fields.year) //overwrites the array
			}
			//month
			if (fields.month != '') {
				filtered = filtered.filter(i => i.month == fields.month)
			}
			//day
			if (fields.day != '') {
				filtered = filtered.filter(i => i.day == fields.day)
			}
			//type
			if (fields.type != '') {
				filtered = filtered.filter(i => i.type == fields.type)
			}
			//desc
			if (fields.desc != '') {
				filtered = filtered.filter(i => i.desc == fields.desc)
			}
			//exvalue
			if (fields.exvalue != '') {
				filtered = filtered.filter(i => i.exvalue == fields.exvalue)
			}
			
			//console.log(filtered) /*after - debug*/
			return filtered
		}

		remove(id){
			localStorage.removeItem(id)
		}
	}

	let db = new Db()

/* Add expense btn 
	CONVERT TO FLASK

	function newexpense(){
		//console.log('Running') //debug
		let year = document.getElementById('year')
		let month = document.getElementById('month')
		let day = document.getElementById('day')
		let type = document.getElementById('type')
		let desc = document.getElementById('desc')
		let exvalue = document.getElementById('exvalue')

		// new object instance of expenses
		let expense = new Expense(
			year.value,
			month.value,
			day.value,
			type.value,
			desc.value,
			exvalue.value
		)

		//console.log(expense) //debug

		if (expense.dataValidation()) {
			//	console.log('dataValidation() pass') //debug
			db.record(expense)
			//	modal instance
			showModal('Recording Success', 'expense save with success!', 'Close', 'success')
			clearFields()

		} else {
			//	console.log('dataValidation() fail') //debug
			//	modal instance
			showModal('Recording error', 'There are mandatory fields that have not been filled in.', 'Go back and fix')
		}
		
	}
*/
/* Expenses List Info 
	CONVERT TO FLASK

	function loadList (expenseList = Array(), filter = false) {
		if (expenseList == 0 && filter == false) {
			expenseList = db.getAll()
		}

		var tbody = document.getElementById('expenseList')		//HTML list
		tbody.innerHTML = ''		//clear HTML element

		expenseList.forEach(function(e){
			//	console.log(e) //debug

			//row
			row = tbody.insertRow()

			//columns
			row.insertCell(0).innerHTML = `${e.year}/${e.month}/${e.day}`	//YYYY-MM-DD
			//type fix
			switch(parseInt(e.type)){
				case 1: e.type = "Food"
					break
				case 2: e.type = "Education"
					break
				case 3: e.type = "Leisure Activities"
					break
				case 4: e.type = "Health"
					break
				case 5: e.type = "Transport"
					break
			}
			row.insertCell(1).innerHTML = e.type
			row.insertCell(2).innerHTML = e.desc
			row.insertCell(3).innerHTML = e.exvalue
			//remove btn
			let removebtn = document.createElement("button")
				removebtn.className = 'btn btn-danger'
				removebtn.innerHTML = '<i class="fas fa-times"></i>'
				removebtn.id = `expense-id_${e.id}`
				removebtn.onclick = function() {
					//console.log(`expense-id_${e.id} removed`) //debug
					db.remove(e.id)
					loadList()
				}
			row.insertCell(4).append(removebtn)
		})

		return expenseList
	}

	/*Filter Function*/
	function expFilter(){
		// console.log('Running') /*debug*/
		let year = document.getElementById('year').value
		let month = document.getElementById('month').value
		let day = document.getElementById('day').value
		let type = document.getElementById('type').value
		let desc = document.getElementById('desc').value
		let exvalue = document.getElementById('exvalue').value

		let fields = new Expense(year, month, day, type, desc, exvalue )

		searchList = db.search(fields)

		loadList(searchList, true)
	}

