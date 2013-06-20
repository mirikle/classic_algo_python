tSort (node* root1, node* root2) {
	stack<node*> s1, s2 ;
	while (true) {
		while (root1) {
			s1.push (root1) ;
			root1 = root1->left ;
		}
		while ( root2 ) {
			s2.push (root2) ;
			root2 = root2->left ;
		}
		if ( s1.empty() && s2.empty() ) 
			break ;
		if ( !s1.empty() && (s2.empty() || s1.top()->val < s2.top()->val)) {
			root1 = s1.top () ;
			printf ( "%d ", s1.top()->val ) ;
			s1.pop () ;
			root1 = root1->right ;
		} else {
			root2 = s2.top () ;
			printf ( "%d ", s2.top()->val ) ;
			s2.pop () ;
			root2 = root2->right ;
		}
	}
	printf ( "\n" ) ;
}


