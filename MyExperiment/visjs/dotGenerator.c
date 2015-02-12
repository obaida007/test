#include <stdio.h>
#include <time.h>
#include <stdlib.h>


int main()
{
int i,j,n,rand1,rand2,r,e;
char ch,ch2;
ch='h';
ch2= 'r';
printf("enter n(host ) and total router r: ");
scanf("%d%d",&n,&r);
printf("n=%d r=%d \n\n",n,r);

for (i=0;i<n;i++)
printf (" %c%d;",ch,i);

printf ("\n\n");

srand(time(NULL));
/*Total number of edges*/
j=0;
for (i=0;i<n;i++)
{
	/*rand1=rand()%n;*/
	rand2=rand()%r;
	printf ("%c%d  -- %c%d; ",ch,j++,ch2,rand2);
}


printf("\n\n");

/*connecting routers, say each router is connected to 3 other routers*/
for (i=0;i<r*3;i++)
{
        rand1=rand()%r;
        rand2=rand()%r;
        printf ("%c%d  -- %c%d; ",ch2,rand1,ch2,rand2);
}

printf("\n\n");
return 0;
}
