% Facts
person(john,30).
person(lisa,25).
person(mike,35).
person(sarah,28).

hobby(john,reading).
hobby(lisa,painting).
hobby(mike,hiking).
hobby(sarah,cooking).

friend(john,lisa).
friend(lisa,sarah).
friend(sarah,mike).

% Rules
adult(X) :- person(X,A), A >= 18.

has_hobby(X,H) :- hobby(X,H).

similar_hobbies(X,Y) :-
    hobby(X,H), hobby(Y,H), X \= Y.

are_friends(X,Y) :- friend(X,Y).
are_friends(X,Y) :- friend(Y,X).

oldest_person(X) :-
    person(X,A),
    \+ (person(_,B), B > A).

friends_of(X,L) :-
    findall(Y, are_friends(X,Y), L).


% swipl -s program.pl - run
% Example queries
% ?- adult(john).
% ?- has_hobby(mike,hiking).
% ?- similar_hobbies(mike,alex).
% ?- are_friends(lisa,john).
% ?- oldest_person(X).
% ?- friends_of(lisa,L).
