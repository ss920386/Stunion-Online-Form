angular.module('MyApp',['ngMaterial','ngMessages','material.svgAssetsCache']).controller('formCtrl',function($scope,$mdDialog){

	$scope.user = {
		content:"",
		category:"",
		suggestions:""
	};

	$scope.$watch("user.category",
		function(newValue,oldValue){
			 console.log( "category changed" );
		}	
	); 

});	