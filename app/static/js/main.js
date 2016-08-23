var app = angular.module('shield',[
	'ngResource', 
	'angularSpinner',
	'jcs-autoValidate',
	'angular-ladda',
	'mgcrea.ngStrap',
	'toaster',
	'ngAnimate'
]);

// app.controller('UserDetailController', function ($scope, ));
app.factory('User', function($http){
	console.log("factory");
	var factory = {};
	factory.addUser = function(info, callback){
		$http.post('/users.json', {user: info}).success(function(data){
			callback(data);
		})
	}
	factory.getUser = function(userId, callback){
		$http.get('/users/' + userId + '.json').success(function(data){
			callback(data);
		})
	}
	return factory;
})

app.controller('ShieldController', function ($scope, $modal, ShieldService) {
	console.log("ShieldController");

	$scope.user = ShieldService;

	$scope.showRgisterModal = function () {
		$scope.createModal = $modal ({
			scope: $scope,
			template: '/views/partials/modal.register.tpl.html',
			show: true
		})
	};

	$scope.registerUser = function () {
		console.log("registerUser");
		$scope.user.createUser($scope.user.selectedUser)
			.then(function () {
				$scope.createModal.hide();
			});
	};
});

app.service('ShieldService', function (User, $q, toaster) {
	console.log("service");
	var self = {
		'addUser': function (user) {
			this.users.push(user);
		},
		'isLoading': false,
		'isSaving': false,
		'isDeleting': false,
		'selectedUser': null,
		'users': [],
		'removeUser': function (user) {
			console.log("remove");
			self.isDeleting = true;
			user.$remove().then(function (){
				self.isDeleting = false;
				var index = self.users.indexOf(user);
				self.users.splice(index,1);
				self.selectedUser = null;
				toaster.pop('success', 'Deleted ' + user.name);
			});
		},
		'createUser': function (user) {
			var d = $q.defer();
			self.isSaving = true;
			User.save(user).$promise.then(function (){
				self.isSaving = false;
				self.selectedUser = null,
				self.users = [];
				toaster.pop('success', 'Created ' + user.name);
				d.resolve()
			});
			return d.promise;
		}
	};
	console.log("service2");
	return self;
})