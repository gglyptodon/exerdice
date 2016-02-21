from django.shortcuts import render
from .models import Die, ExerciseDefinition, ExerciseTask, Workout
from .forms import WorkoutForm
from django.shortcuts import get_object_or_404, render, redirect, render_to_response

from django.template import RequestContext
import random

def index(request):
    result_list = Die.objects.all()  # all the results
    context = {'result_list': result_list}
    return render(request, 'exerdice_core/index.html', context)


def roll(request):
    if request.method == "POST":
        form = WorkoutForm(request.POST)
        if form.is_valid():  # todo refactor cleaning up
            new = Workout.objects.create()
            print(new)
            num_task = random.randint(1,5)+random.randint(1,5)
            for _ in xrange(num_task):
                e = ExerciseTask()
                eid = random.choice([s.id for s in ExerciseDefinition.objects.all()])
                e.exercise_id  = eid
                e.save()
                new.exercise_tasks.add(e)
                new.save()
            print(new)

            #tmp_up = request.POST['up']
            #newupload.up = sanitize_txt(tmp_up)
            #tmp_down = request.POST['down']
            #newupload.down = sanitize_txt(tmp_down)
            #newupload.save()
            ## todo select reference!
            #reference = ReferenceData.objects.get(name="ATH1.csv").csv._get_path()
            # now run the physioprocessor!
            #print(newupload.down, newupload.down.split(","))
            #print(newupload.up, newupload.up.split(","))
            #result_values, result_rownames, result_colnames = get_physioprocessor_result_from_lists(
            #    reference_csv=reference, submission_up=newupload.up.split(','),
            #    submission_down=newupload.down.split(',')
            #)
            # todo visualize
            #palette = get_colorpalette_from_string(request.POST['colorscheme'])
            #palette = bokeh.palettes.YlOrRd9

            # print(result_rownames, result_colnames)
            #if not result_colnames:
            #    result_colnames = ["NA"]  # *30# len(newupload.up)
            #df = pandas.DataFrame(result_values, index=result_rownames, columns=result_colnames)
#
            #hm = HeatMap(df, title="", palette=palette, height=1000, width=1000)

            #script, div = components(hm)
            #new_result_object = ResultData()
            #new_result_object.id = str(uuid.uuid4())
            #new_result_object.data = script
            #new_result_object.divdata = div
            # print(df)
            # print(df.to_csv())
            #new_result_object.csvdata = str(df.to_csv())
            #new_result_object.save()
            #if ResultData.objects.all().count() > 2:  # delete old entries
                # startdate = datetime.date.today()- datetime.timedelta(days=2)
                #enddate = datetime.date.today() - datetime.timedelta(days=1)
                #print("delete{}".format(ResultData.objects.filter(created_on__lt=enddate)))
                #ResultData.objects.filter(created_on__lt=enddate).delete()
    #
            return redirect('/detail/'+str(new.id)+"/")  # redirect to .views.thanks
    else:
         form = WorkoutForm()
    #
    return render_to_response('exerdice_core/roll.html', {'form': form}, RequestContext(request))
    #
    #





def detail(request, detail_id):
    result = get_object_or_404(Workout , pk=detail_id)
    print(result, "RESULT")
    tsk = result.exercise_tasks.all()
    bla = ", ".join([str(t) for t in tsk])
    print("bla",bla)
    return render(request, 'exerdice_core/detail.html', {'result': tsk, 'bla':bla})