import java.util.ArrayList;

public class Zajęcia {
    private ArrayList<Student> students = new ArrayList<Student>();

    public void zapiszStudenta(Student Student){
            if(this.students.size()<10){
                this.students.add(Student);
            }
            else{System.out.println("Za dużo Studentów w grupie!");}
    }
}
