
% Facts
person(john,30).
person(lisa,25).
person(mike,35).

hobby(john,reading).
hobby(lisa,painting).
hobby(mike,reading).

friend(john,lisa).
friend(lisa,mike).

% Rules
adult(X) :-
    person(X,A),
    A >= 18.

similar_hobbies(X,Y) :-
    hobby(X,H),
    hobby(Y,H),
    X \= Y.

are_friends(X,Y) :- friend(X,Y).
are_friends(X,Y) :- friend(Y,X).

oldest_person(X) :-
    person(X,A),
    \+ (person(_,B), B > A).

check_name(X) :-
    person(X,_).



% adult(john).
% adult(lisa).

% similar_hobbies(john,mike).

% are_friends(john,lisa).
% are_friends(mike,lisa).

% oldest_person(X).

% check_name(john).
% check_name(raj).
