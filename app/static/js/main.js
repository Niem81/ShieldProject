var app = angular.module('shield',[
	'ngResource',
	'infinite-scroll',
	'angularSpinner',
	'jcs-autoValidate',
	'angular-ladda',
	'mgcrea.ngStrap',
	'toaster',
	'ngAnimate',
	'ui.router'
]);

app.config(function ($stateProvider, $urlRouterProvider) {
	$stateProvider
		.state('home', {
			url: "/",
			templateUrl: 'index.html',
			controller: 'ShieldController'
		})
		.state('editar', {
			url: "/edit/:email",
			views: {
				'main': {
					templateUrl: 'templates/edit.html',
					controller: 'PersonDetailController'
				}
			}
		})
		.state('crear', {
			url:"/create",
			views: {
				'main': {
					templateUrl: 'templates/edit.html',
					controller: 'PersonCreateController'
				}
			}
		})
		.state('second', {
			url: "/users/home",
			templateUrl: '2.html'
		});
	$urlRouterProvider.otherwise('/');
});

app.config(function ($httpProvider, laddaProvider, $datepickerProvider) {
	//Enable cross domain calls
    $httpProvider.defaults.useXDomain = true;
 	console.log("config");
	laddaProvider.setOption({
		style: 'expand-right'
	});
	angular.extend($datepickerProvider.defaults, {
		dateFormat: 'd/M/yyyy',
		autoclose: true
	});
	console.log("config2");
});

app.factory('userFactory', function($http){
	console.log("userFactory");
	var factory = {};
	factory.addUser = function(info, callback){
		console.log("inside addUser");
		console.log(info);
		$http
		({
		    method: 'POST',
		    url: '/users/register',
		    data: info,
		    headers: {'Content-Type': 'application/x-www-form-urlencoded'},
		    transformRequest: function(obj) {
				var str = [];
				for(var p in obj)
				str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
				return str.join("&");
		    }
		})
		.success(function(data){
			console.log("did it");
			console.log(data.status);
			console.log(data);
		  	callback(data);
		})
	}
	// factory.getUser = function(userId, callback){
	// 	$http.get('/users/' + userId + '.json').success(function(data){
	// 		callback(data);
	// 	})
	// }
	return factory;
});

app.factory('sessionFactory', function($http){	
		var factory = {}
		factory.loginUser = function(info, callback){
			$http.post('/sessions.json', {user: info}).success(function(data){
				console.log(data);
				//callback(data);
			})
		}
		return factory
	});

app.controller('ShieldController', function ($scope, $modal, $state, ShieldUserService) {
	console.log("ShieldController");

	$scope.user = ShieldUserService;

	$scope.showRegisterModal = function () {
		$scope.user.selectedUser = {}
		$scope.createModal = $modal ({
			scope: $scope,
			template: '../static/partials/modal.register.tpl.html',
			show: true
		})
	};

	$scope.registerUser = function () {
		console.log("registerUser");
		console.log($scope.user.selectedUser);
		var log = $scope.user.createUser($scope.user.selectedUser); 
		if (log) {
				console.log("getting data");
				console.log(log);
				$scope.createModal.hide();
				//$state.go("home");
			};
	};

	$scope.showLoginModal = function () {
		$scope.createModal = $modal ({
			scope: $scope,
			template: '../static/partials/modal.login.tpl.html',
			show: true
		})
	};

	$scope.loginUser = function () {
		$scope.user.loginUser($scope.user.selectedUser)
			.then(function () {
				$scope.createModal.hide();
			});
	};
});

app.service('ShieldUserService', function (userFactory, $q, toaster) {
	console.log("service");
	var userF = userFactory;
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
			//var d = $q.defer();
			var data = {};
			self.isSaving = true;
			console.log("Before using addUser");
			userFactory.addUser(user, function (data){
				if(data.status == 'OK'){
					console.log("inside mthod service!");
					console.log(data);
					data = data;
					self.isSaving = false;
					self.selectedUser = null,
					toaster.pop('success', 'Created ' + data.message);
					
				}
			});
			return data;
			//return d.promise;
		}
	};
	console.log("service2");
	return self;
});