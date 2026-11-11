% Facts
male(ram).
male(raj).
male(kumar).

female(sita).
female(geetha).
female(priya).

parent(ram, raj).
parent(sita, raj).

parent(raj, kumar).
parent(geetha, kumar).

parent(kumar, priya).

% Rules

% X is a father of Y
father(X,Y) :-
    male(X),
    parent(X,Y).

% X is a mother of Y
mother(X,Y) :-
    female(X),
    parent(X,Y).

% X is a child of Y
child(X,Y) :-
    parent(Y,X).

% X is a grandfather of Y
grandfather(X,Y) :-
    male(X),
    parent(X,Z),
    parent(Z,Y).

% X is a grandmother of Y
grandmother(X,Y) :-
    female(X),
    parent(X,Z),
    parent(Z,Y).

% X is a sibling of Y
sibling(X,Y) :-
    parent(Z,X),
    parent(Z,Y),
    X \= Y.

% X is an ancestor of Y
ancestor(X,Y) :-
    parent(X,Y).

ancestor(X,Y) :-
    parent(X,Z),
    ancestor(Z,Y).
