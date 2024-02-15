public class evenAdd
{
public void even()
{
for(int x = 2;x<200;x++)
if (x%2==0)
System.out.println(x);
}
public void odd(){

int x = 1;
while(x<350){
if(x%2==0){
System.out.print("");

}
else
System.out.println(x + " It is odd");
x+=1;
}
}
public static void main(String[] args){
evenAdd d = new evenAdd();
d.even();
d.odd();
}
}
