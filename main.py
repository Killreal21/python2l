
#2.1
def f21 (a,b,c,d,e):
    if (a=='vcl' or b=='vcl' or c=='vcl' or d=='vcl' or e=='vcl'):
        return 6
    else: #возможно поменять на елиф
        if (a==2002 or b==2002 or c==2002 or d==20002 or e==2002):
            if (a=='cmake' or b=='cmake' or c=='cmake' or d=='cmake' or e=='cmake'):
                return 4
            elif(a=='ruby' or b=='ruby' or c=='ruby' or d=='ruby' or e=='ruby'):
                return 5
        else:
            if(a=='nu' or b=='nu' or c=='nu' or d=='nu' or e=='nu'):
                if(a=='scss' or b=='scss' or c=='scss' or d=='scss' or e=='scss'):
                    return 0
                else:
                    return 1
            else:
                if (a == 'scss' or b == 'scss' or c == 'scss' or d == 'scss' or e == 'scss'):
                    return 2
                else:
                    return 3

print(f21(a='m4',b='vcl',c='haxe',d='ruby', e=2002))