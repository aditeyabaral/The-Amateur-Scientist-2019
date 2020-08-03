#include<stdio.h>

int find(char *text,char target,int size)
{
   for (int i=0;i<size;i++)
   {
      if (text[i]==target)
         return i;
   }
}


int main()
{
   char plaintext[30],cyphertext[30],text[300],crypt[300],option;
   int a,b;
   printf("Would you like to encrypt [E] or decrypt [D] using Affine cypher?\n");
   scanf(" %c",&option);
   printf("Enter values of 'a' and 'b'\n");
   scanf("%d%d",&a,&b);
   for (int i=0; i<26;i++)
   {
      plaintext[i] = (char)(i+'a');
      cyphertext[i] = (char)((a*i+b)%26+'a');
   }
   plaintext[26]='\0';
   cyphertext[26]='\0';
   
   if (option=='E' || option=='e')
   {
      printf("Enter text to encrypt\n");
      scanf("%s",text);
      int i=0,j=0;
      while (text[i]!='\0')
      {
         if (text[i]>96&&text[i]<123)
         {
            crypt[j]=cyphertext[text[i]-'a'];
            j++;
         }
         else if (text[i]>64&&text[i]<91)
         {
            crypt[j]=cyphertext[text[i]-'A'];
            j++;
         }
         i++;
      }
      crypt[j]='\0';
   }
   else if (option=='D' || option=='d')
   {
      printf("Enter text to decrypt\n");
      scanf("%s",text);
      int i=0,j=0;
      while (text[i]!='\0')
      {
          if (text[i]>96&&text[i]<123)
         {
            crypt[j]=plaintext[find(cyphertext,text[i],30)];
            j++;
         }
         else if (text[i]>64&&text[i]<91)
         {
            crypt[j]=plaintext[find(cyphertext,text[i]-'A'+'a',30)];
            j++;
         }
         i++;
      }
      crypt[j]='\0';
   }
   else
      printf("Invalid option\n");
   
    printf("%s\n",crypt);
   
//    printf("%s\n%s\n",plaintext,cyphertext);
   
   return 0;
}
